import streamlit as st


def render_audio_file_info(uploaded_file):
    file_size_mb = round(uploaded_file.size / (1024 * 1024), 3)
    file_type = uploaded_file.type if uploaded_file.type else "Unknown"

    st.markdown('<div class="section-title">Audio File Details</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">File Name</div>
            <div class="card-value blue" style="font-size:22px;">{uploaded_file.name}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">File Size</div>
            <div class="card-value green">{file_size_mb} MB</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">File Type</div>
            <div class="card-value orange" style="font-size:22px;">{file_type}</div>
        </div>
        """, unsafe_allow_html=True)