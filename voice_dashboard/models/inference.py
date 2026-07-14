import time
import tempfile
import librosa

import streamlit as st
import torch
import torchaudio
from transformers import WavLMForSequenceClassification


CONFIG = {
    "target_sample_rate": 16000,
    "max_duration": 4,
    "model_name": "microsoft/wavlm-base",
    "model_path": "models/best_wavlm_model.pt"
}


@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = WavLMForSequenceClassification.from_pretrained(
        CONFIG["model_name"],
        num_labels=2
    )

    model.load_state_dict(
        torch.load(CONFIG["model_path"], map_location=device)
    )

    model.to(device)
    model.eval()

    return model, device


def predict_single_file(file_path, model, device, config):
    target_sample_rate = config["target_sample_rate"]
    max_duration = config["max_duration"]
    max_length = target_sample_rate * max_duration

    audio, sample_rate = librosa.load(
    file_path,
    sr=config["target_sample_rate"],
    mono=True
)

    waveform = torch.tensor(audio, dtype=torch.float32).unsqueeze(0)

    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    

    waveform = waveform.squeeze(0)
    original_length = waveform.shape[0]
    duration = round(original_length / target_sample_rate, 2)

    if original_length > max_length:
        start = (original_length - max_length) // 2
        waveform = waveform[start:start + max_length]
        attention_mask = torch.ones(max_length, dtype=torch.long)
    else:
        pad_length = max_length - original_length
        waveform = torch.nn.functional.pad(waveform, (0, pad_length))
        attention_mask = torch.cat([
            torch.ones(original_length, dtype=torch.long),
            torch.zeros(pad_length, dtype=torch.long)
        ])

    input_values = waveform.unsqueeze(0).to(device)
    attention_mask = attention_mask.unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(
            input_values=input_values,
            attention_mask=attention_mask
        )
        probs = torch.softmax(outputs.logits, dim=-1)[0]

    pred_class = torch.argmax(probs).item()

    return {
        "prediction": "FAKE" if pred_class == 1 else "REAL",
        "p_real": float(probs[0].item()),
        "p_fake": float(probs[1].item()),
        "duration": duration
    }


def predict_uploaded_audio(uploaded_file):
    start_time = time.time()

    suffix = "." + uploaded_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        temp_path = tmp.name

    model, device = load_model()
    raw_result = predict_single_file(temp_path, model, device, CONFIG)

    p_real = raw_result["p_real"]
    p_fake = raw_result["p_fake"]

    prediction = "Spoof Detected" if raw_result["prediction"] == "FAKE" else "Real"
    confidence = round(max(p_real, p_fake) * 100, 2)
    real_prob = round(p_real * 100, 2)
    fake_prob = round(p_fake * 100, 2)

    if prediction == "Spoof Detected":
        risk_level = "HIGH" if confidence >= 80 else "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "prediction": prediction,
        "risk_level": risk_level,
        "confidence": confidence,
        "real_prob": real_prob,
        "fake_prob": fake_prob,
        "model_name": "WavLM",
        "processing_time": round(time.time() - start_time, 3),
        "duration": raw_result["duration"]
    }