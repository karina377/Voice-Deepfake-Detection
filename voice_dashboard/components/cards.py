import streamlit as st


def get_recommendation(prediction: str):
    if prediction == "Spoof Detected":
        return "High confidence deepfake detected. Verify the speaker using an additional authentication method before approving sensitive actions."
    return "The recording appears authentic. No immediate action is required."


def render_result_panel(result):
    prediction = result["prediction"]
    confidence = result["confidence"]
    risk_level = result["risk_level"]
    model_name = result["model_name"]
    real_prob = result["real_prob"]
    fake_prob = result["fake_prob"]
    processing_time = result["processing_time"]
    recording_id = result.get("recording_id", "N/A")
    timestamp = result.get("timestamp", "N/A")

    if prediction == "Spoof Detected":
        banner_class = "soc-alert-danger"
        icon = "🔴"
        title = "התראה חמורה: הקלטה מזויפת (Spoof Detected)"
    else:
        banner_class = "soc-alert-safe"
        icon = "🟢"
        title = "הקלטה תקינה: לא זוהה זיוף (Real Recording)"

    st.markdown(f"""
    <div class="{banner_class}">
        {icon} {title}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="soc-card">
            <div class="soc-card-title">רמת סיכון עסקית (Risk Level)</div>
            <div class="soc-card-value">{risk_level}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="soc-card">
            <div class="soc-card-title">ציון ביטחון (Confidence Score)</div>
            <div class="soc-card-value">{confidence}%</div>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"""
        <div class="soc-card">
            <div class="soc-card-title">מודל שביצע את הזיהוי</div>
            <div class="soc-card-value">{model_name} ✓</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="soc-card">
            <div class="soc-card-title">הסתברויות סיווג (Probabilities)</div>
            <div class="soc-card-value small">
                <span class="green">Real: {real_prob}%</span><br>
                <span class="red">Fake: {fake_prob}%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:
        st.markdown(f"""
        <div class="soc-card">
            <div class="soc-card-title">זמן עיבוד (Processing Time)</div>
            <div class="soc-card-value">{processing_time} sec</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown(f"""
        <div class="soc-card">
            <div class="soc-card-title">מזהה הקלטה (Recording ID)</div>
            <div class="soc-card-value small">{recording_id}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="soc-wide-card">
        <div>
            <b>תאריך ושעה (Timestamp)</b><br>
            {timestamp}
        </div>
        <div>
            <b>AI Recommendation</b><br>
            {get_recommendation(prediction)}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_metric_cards(model_name, processing_time, duration, file_size):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Model", model_name)
    col2.metric("Processing Time", f"{processing_time} sec")
    col3.metric("Duration", f"{duration} sec")
    col4.metric("File Size", f"{file_size} MB")