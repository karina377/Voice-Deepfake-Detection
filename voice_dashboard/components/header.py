import streamlit as st


def render_header():
    st.markdown("""
    <div class="main-header">
        <div>
            <div class="main-title">🛡️ SmartDetect AI</div>
            <div class="main-subtitle">Real-Time Voice Deepfake Detection</div>
        </div>
        <div class="header-status">🟢 Online</div>
    </div>
    """, unsafe_allow_html=True)