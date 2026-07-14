import streamlit as st


def render_kpi_bar(stats):
    st.markdown('<div class="section-title">System Overview</div>', unsafe_allow_html=True)

    total = max(stats["total"], 1)
    real_percent = (stats["real"] / total) * 100
    fake_percent = (stats["fake"] / total) * 100

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Audio Files Checked</div>
            <div class="kpi-value">{stats["total"]}</div>
            <div class="kpi-subtext">Since launch</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Real Recordings</div>
            <div class="kpi-value green">{stats["real"]}</div>
            <div class="kpi-subtext green">{real_percent:.1f}% of all analyses</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Deepfake Recordings</div>
            <div class="kpi-value red">{stats["fake"]}</div>
            <div class="kpi-subtext red">{fake_percent:.1f}% of all analyses</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Average Confidence</div>
            <div class="kpi-value blue">{stats["avg_confidence"]:.2f}%</div>
            <div class="kpi-subtext">Overall average</div>
        </div>
        """, unsafe_allow_html=True)

    with k5:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Average Model Processing Time</div>
            <div class="kpi-value orange">{stats["avg_processing_time"]:.2f} sec</div>
            <div class="kpi-subtext">Per audio file</div>
        </div>
        """, unsafe_allow_html=True)