import streamlit as st
import uuid

from datetime import datetime
from components.header import render_header
from models.inference import predict_uploaded_audio
from components.kpi import render_kpi_bar
from components.cards import render_result_panel, render_metric_cards
from components.charts import render_probability_chart, render_database_charts
from components.history import render_statistics, render_history_table,render_last_statistics

from database import init_db, insert_prediction, get_history, get_statistics, clear_history


from pathlib import Path
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent


def load_css(filename: str) -> None:
    file_path = BASE_DIR / filename

    with open(file_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


st.set_page_config(
    page_title="AI Voice Deepfake Detection",
    page_icon="🎙️",
    layout="wide"
)

load_css("style.css")
init_db()

# ---------- Sidebar ----------
st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="sidebar-logo">🛡️</div>
    <div>
        <div class="sidebar-title">SmartDetect AI</div>
        <div class="sidebar-subtitle">Real-Time Voice Deepfake Detection</div>
    </div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "📊 Analytics", "🗄 History", "ℹ️ About"],
    label_visibility="collapsed"
)

page = (
    page.replace("🏠 ", "")
        .replace("📊 ", "")
        .replace("🗄 ", "")
        .replace("ℹ️ ", "")
)

current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M")
st.sidebar.markdown(f"""
<div class="sidebar-status-card">
    <div class="status-title">System Status</div>
    <div class="status-row">🟢 All Systems Operational</div>
    <div class="status-divider"></div>
    <div class="status-row">📅 Current Date & Time<br><b>{current_datetime}</b></div>
    <div class="status-row">🛡️ Model<br><b>WavLM</b></div>
</div>
""", unsafe_allow_html=True)


# ---------- Dashboard Page ----------
if page == "Dashboard":
    render_header()
    stats = get_statistics()
    render_kpi_bar(stats)

    left_col, right_col = st.columns([1, 1.25])

    with left_col:
        st.markdown("""
        <div class="upload-panel">
            <div class="panel-title">📂 Upload Audio</div>
            <div class="panel-subtitle">
                Upload a voice recording for real-time deepfake detection.
            </div>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Upload audio file",
            type=["wav", "mp3", "flac", "m4a"],
            label_visibility="collapsed"
        )

        analyze_clicked = False

        if uploaded_file is not None:
            file_size_mb = round(uploaded_file.size / (1024 * 1024), 3)
            file_format = uploaded_file.name.split(".")[-1].upper()

            st.audio(uploaded_file)

            st.markdown(f"""
            <div class="card">
                <div class="card-title">Audio Information</div>
                <div class="recommendation-text">
                    <b>Format:</b> {file_format}<br>
                    <b>File Size:</b> {file_size_mb} MB<br>
                    <b>Model:</b> WavLM<br>
                    <b>Mode:</b> Real-Time Inference
                </div>
            </div>
            """, unsafe_allow_html=True)

            analyze_clicked = st.button("🔍 Analyze Recording", use_container_width=True)

        else:# אם אין קובץ – נאפס את תוצאת הניתוח האחרונה
            if "last_result" in st.session_state:
                del st.session_state["last_result"]

            st.info("Please upload an audio file to start analysis.")

    with right_col:
        st.markdown(
            '<div class="system-status">🟢 System Online | Model Ready | Database Connected</div>',
            unsafe_allow_html=True
        )

        if "last_result" not in st.session_state:
            st.markdown("""
            <div class="result-panel">
                <div class="result-label">Analysis Result</div>
                <div class="result-main">Waiting for audio...</div>
                <div class="recommendation-text">
                    Upload an audio file and click Analyze Recording to view the prediction result.
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            result = st.session_state["last_result"]
            render_result_panel(result)

    if uploaded_file is not None and analyze_clicked:
        recording_id = f"REC-{uuid.uuid4().hex[:8].upper()}"

        with st.spinner("Analyzing audio with WavLM..."):
            model_result = predict_uploaded_audio(uploaded_file)

        prediction = model_result["prediction"]
        risk_level = model_result["risk_level"]
        confidence = model_result["confidence"]
        real_prob = model_result["real_prob"]
        fake_prob = model_result["fake_prob"]
        model_name = model_result["model_name"]
        processing_time = model_result["processing_time"]
        duration = model_result["duration"]

        file_size_mb = round(uploaded_file.size / (1024 * 1024), 3)

        insert_prediction(
            recording_id=recording_id,
            filename=uploaded_file.name,
            prediction=prediction,
            risk_level=risk_level,
            confidence=confidence,
            real_probability=real_prob,
            fake_probability=fake_prob,
            model_name=model_name,
            processing_time=processing_time
        )

        st.session_state["last_result"] = {
            "prediction": prediction,
            "risk_level": risk_level,
            "confidence": confidence,
            "real_prob": real_prob,
            "fake_prob": fake_prob,
            "model_name": model_name,
            "processing_time": processing_time,
            "duration": duration,
            "file_size": file_size_mb,
            "recording_id": recording_id,
            "timestamp": datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
        }

        st.rerun()

    if "last_result" in st.session_state:
        result = st.session_state["last_result"]

        st.markdown('<div class="section-title">Detection Summary</div>', unsafe_allow_html=True)

        render_metric_cards(
            result["model_name"],
            result["processing_time"],
            result["duration"],
            result["file_size"]
        )

        render_probability_chart(result["real_prob"], result["fake_prob"])


# ---------- Analytics Page ----------
elif page == "Analytics":
    render_header()
    stats = get_statistics()
    render_kpi_bar(stats)

    history_df = get_history()

    if "last_result" in st.session_state:
        render_last_statistics(st.session_state["last_result"])
    else:
        st.info("No audio files have been analyzed yet.")

    render_database_charts(history_df)


# ---------- History Page ----------
elif page == "History":
    render_header()
    stats = get_statistics()
    render_kpi_bar(stats)

    if st.button("🗑️ Clear History"):
        clear_history()
        st.session_state.pop("last_result", None)
        st.success("History deleted successfully.")
        st.rerun()

    history_df = get_history()
    render_history_table(history_df)


# ---------- About Page ----------
elif page == "About":
    render_header()

    st.markdown("# 🎙️ SmartDetect AI")

    st.write("""
SmartDetect AI is a real-time voice deepfake detection platform developed
as a Final Project in Information Systems at The Max Stern Yezreel Valley College.

The system analyzes uploaded voice recordings using a fine-tuned WavLM model
and classifies each recording as either Real or Spoof Detected.
""")

    st.markdown("---")
    st.subheader("👩‍💻 About the Team")

    st.write("""
SmartDetect AI was developed by **Karina Pisarenko** and **Nofar Horada**
as part of a final-year Information Systems project.

Our goal is to develop an AI-powered system capable of detecting synthetic
and deepfake voice recordings in real time using advanced deep learning techniques.
""")

    st.markdown("---")
    st.subheader("📬 Contact")
    
    st.markdown("""
**🎓 Institution**  
The Max Stern Yezreel Valley College

**👩‍🎓 Students**  
Karina Pisarenko  
Nofar Horada

**👩‍🏫 Supervisor**  
Keren Segal

**📧 Email**  
karinasmile2014@gmail.com  
nofar8659@gmail.com
""")
                
    st.markdown("---")
    
    st.subheader("📊 WavLM Model Performance")
    
    metrics = [
        ("Accuracy", 99.40),
        ("Precision", 99.85),
        ("Recall", 98.95),
        ("F1-Score", 99.40),
        ("ROC-AUC", 99.91)
    ]
    
    cols = st.columns(5)
    
    for col, (name, value) in zip(cols, metrics):
        with col:
            # ה-HTML מוצמד לחלוטין לשמאל כדי למנוע מ-Streamlit להציג אותו כטקסט קוד
            st.markdown(f"""
<div style="border: 1px solid #E5E7EB; border-radius: 14px; padding: 18px; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.05); text-align: center; height: 250px; min-width: 0; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; align-items: center;">
<h4 style="margin: 0; padding-top: 10px;">{name}</h4>
<div style="height: 100px; display: flex; align-items: center; justify-content: center; width: 100%; overflow: hidden;">
    <div style="color: #1976D2; margin: 0; width: 100%; text-align: center; white-space: nowrap; font-size: clamp(30px, 2.1vw, 44px); line-height: 1; font-weight: 800; font-variant-numeric: tabular-nums;">
        {value:.2f}%
    </div>
</div>
<div style="width: 100%; margin-bottom: 10px;">
<div style="width: 100%; height: 10px; background: #AEB6C2; border-radius: 8px; overflow: hidden;">
<div style="width: {value}%; height: 100%; background: #1976D2; border-radius: 8px;"></div>
</div>
<div style="display: flex; justify-content: space-between; font-size: 11px; color: #8A8A8A; margin-top: 4px;">
<span>0</span>
<span>100</span>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("⚙️ Model Configuration")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**Model:** WavLM  
**Framework:** PyTorch  
**Sample Rate:** 16 kHz
""")

    with col2:
        st.markdown("""
**Max Audio Length:** 4 Seconds  
**Output Classes:** Real / Spoof Detected  
**Database:** SQLite
""")

    st.markdown("---")
    st.subheader("🔄 System Workflow")

    st.code("""
Upload Audio
      │
      ▼
Audio Preprocessing
      │
      ▼
WavLM Deep Learning Model
      │
      ▼
Prediction (Real / Spoof Detected)
      │
      ▼
SQLite Database
      │
      ▼
Interactive Dashboard
""")