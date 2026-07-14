import os
import time
import tempfile
from pathlib import Path

import gdown
import librosa
import streamlit as st
import torch
from transformers import WavLMForSequenceClassification


# =========================================================
# Paths and configuration
# =========================================================

# התיקייה שבה נמצא inference.py
BASE_DIR = Path(__file__).resolve().parent

# המודל יישמר בתוך voice_dashboard/models
MODEL_PATH = BASE_DIR / "best_wavlm_model.pt"

CONFIG = {
    "target_sample_rate": 16000,
    "max_duration": 4,
    "model_name": "microsoft/wavlm-base",
    "model_path": str(MODEL_PATH),


    "model_drive_url": "https://drive.google.com/file/d/1fEh_y0MqQUDYNP7zRR8N3DKctvlC06Z5/view?usp=sharing"
}


# =========================================================
# Download model from Google Drive
# =========================================================

def ensure_model_exists() -> Path:
    """
    בודקת אם קובץ המודל קיים.
    אם הוא לא קיים, מורידה אותו מ-Google Drive.
    """

    model_path = Path(CONFIG["model_path"])

    if model_path.exists() and model_path.stat().st_size > 1_000_000:
        return model_path

    model_path.parent.mkdir(parents=True, exist_ok=True)

    drive_url = CONFIG["model_drive_url"]

    if (
        not drive_url
        or drive_url == "PASTE_GOOGLE_DRIVE_LINK_HERE"
    ):
        raise RuntimeError(
            "Google Drive model link is missing in inference.py."
        )

    st.write("Step 1: Downloading trained model from Google Drive...")

    downloaded_file = gdown.download(
        url=drive_url,
        output=str(model_path),
        quiet=False,
        fuzzy=True
    )

    if downloaded_file is None:
        raise RuntimeError(
            "Model download failed. "
            "Make sure the Google Drive file is shared with anyone who has the link."
        )

    if not model_path.exists():
        raise RuntimeError(
            "The model file was not created after download."
        )

    if model_path.stat().st_size < 1_000_000:
        model_path.unlink(missing_ok=True)

        raise RuntimeError(
            "The downloaded file is too small and is probably not the model. "
            "Check the Google Drive sharing permissions and link."
        )

    st.write(
        f"Step 2: Model downloaded successfully "
        f"({model_path.stat().st_size / (1024 ** 2):.1f} MB)."
    )

    return model_path


# =========================================================
# Load trained WavLM model
# =========================================================

@st.cache_resource(show_spinner="Loading WavLM model...")
def load_model():
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    st.write(f"Using device: {device}")

    model_path = ensure_model_exists()

    st.write("Step 3: Loading WavLM architecture from Hugging Face...")

    model = WavLMForSequenceClassification.from_pretrained(
        CONFIG["model_name"],
        num_labels=2
    )

    st.write("Step 4: WavLM architecture loaded.")

    st.write("Step 5: Reading trained checkpoint...")

    checkpoint = torch.load(
        model_path,
        map_location="cpu",
        weights_only=False
    )

    st.write("Step 6: Checkpoint loaded into memory.")

    # תמיכה בצורות שמירה שונות
    if isinstance(checkpoint, dict):
        if "state_dict" in checkpoint:
            checkpoint = checkpoint["state_dict"]
        elif "model_state_dict" in checkpoint:
            checkpoint = checkpoint["model_state_dict"]

    st.write("Step 7: Applying trained weights...")

    model.load_state_dict(checkpoint)

    model.to(device)
    model.eval()

    st.write("Step 8: Model loaded successfully.")

    return model, device


# =========================================================
# Audio preprocessing and prediction
# =========================================================

def predict_single_file(file_path, model, device, config):
    target_sample_rate = config["target_sample_rate"]
    max_duration = config["max_duration"]
    max_length = target_sample_rate * max_duration

    audio, _ = librosa.load(
        file_path,
        sr=target_sample_rate,
        mono=True
    )

    if audio.size == 0:
        raise ValueError("The uploaded audio file is empty.")

    waveform = torch.tensor(
        audio,
        dtype=torch.float32
    )

    original_length = waveform.shape[0]
    duration = round(
        original_length / target_sample_rate,
        2
    )

    if original_length > max_length:
        start = (original_length - max_length) // 2
        waveform = waveform[start:start + max_length]

        attention_mask = torch.ones(
            max_length,
            dtype=torch.long
        )

    else:
        pad_length = max_length - original_length

        waveform = torch.nn.functional.pad(
            waveform,
            (0, pad_length)
        )

        attention_mask = torch.cat([
            torch.ones(
                original_length,
                dtype=torch.long
            ),
            torch.zeros(
                pad_length,
                dtype=torch.long
            )
        ])

    input_values = waveform.unsqueeze(0).to(device)
    attention_mask = attention_mask.unsqueeze(0).to(device)

    with torch.inference_mode():
        outputs = model(
            input_values=input_values,
            attention_mask=attention_mask
        )

        probabilities = torch.softmax(
            outputs.logits,
            dim=-1
        )[0]

    predicted_class = torch.argmax(
        probabilities
    ).item()

    return {
        "prediction": (
            "FAKE"
            if predicted_class == 1
            else "REAL"
        ),
        "p_real": float(probabilities[0].item()),
        "p_fake": float(probabilities[1].item()),
        "duration": duration
    }


# =========================================================
# Streamlit uploaded-file prediction
# =========================================================

def predict_uploaded_audio(uploaded_file):
    start_time = time.time()

    if uploaded_file is None:
        raise ValueError("No audio file was uploaded.")

    suffix = Path(
        uploaded_file.name or "uploaded_audio.wav"
    ).suffix

    if not suffix:
        suffix = ".wav"

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_path = temp_file.name

        model, device = load_model()

        raw_result = predict_single_file(
            file_path=temp_path,
            model=model,
            device=device,
            config=CONFIG
        )

        p_real = raw_result["p_real"]
        p_fake = raw_result["p_fake"]

        prediction = (
            "Spoof Detected"
            if raw_result["prediction"] == "FAKE"
            else "Real"
        )

        confidence = round(
            max(p_real, p_fake) * 100,
            2
        )

        real_prob = round(
            p_real * 100,
            2
        )

        fake_prob = round(
            p_fake * 100,
            2
        )

        if prediction == "Spoof Detected":
            risk_level = (
                "HIGH"
                if confidence >= 80
                else "MEDIUM"
            )
        else:
            risk_level = "LOW"

        return {
            "prediction": prediction,
            "risk_level": risk_level,
            "confidence": confidence,
            "real_prob": real_prob,
            "fake_prob": fake_prob,
            "model_name": "WavLM",
            "processing_time": round(
                time.time() - start_time,
                3
            ),
            "duration": raw_result["duration"]
        }

    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass