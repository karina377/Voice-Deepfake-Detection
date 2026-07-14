import streamlit as st


def render_statistics(stats):
    st.markdown('<div class="section-title">Management Statistics</div>', unsafe_allow_html=True)

    s1, s2, s3, s4, s5 = st.columns(5)

    s1.metric("Audio Files Checked", stats["total"])
    s2.metric("Authentic", stats["real"])
    s3.metric("Spoofed", stats["fake"])
    s4.metric("Average Confidence", f'{stats["avg_confidence"]}%')
    s5.metric("Average Processing Time", f'{stats["avg_processing_time"]} sec')


def render_history_table(history_df):
    st.markdown('<div class="section-title">Prediction History</div>', unsafe_allow_html=True)

    if history_df.empty:
        st.info("No analysis history yet.")
        return

    col1, col2 = st.columns([2, 1])

    with col1:
        search_text = st.text_input("Search by file name or recording ID")

    with col2:
        prediction_filter = st.selectbox(
            "Filter by prediction",
            ["All", "Spoof Detected", "Real"]
        )

    filtered_df = history_df.copy()

    if search_text:
        filtered_df = filtered_df[
            filtered_df["Recording ID"].astype(str).str.contains(search_text, case=False, na=False) |
            filtered_df["File Name"].astype(str).str.contains(search_text, case=False, na=False)
        ]

    if prediction_filter != "All":
        filtered_df = filtered_df[filtered_df["Prediction"] == prediction_filter]

    st.dataframe(filtered_df, use_container_width=True)

    st.caption(f"Showing {len(filtered_df)} of {len(history_df)} records.")



def render_last_statistics(result):
    st.markdown('<div class="section-title">Last Analysis Summary</div>', unsafe_allow_html=True)

    if not result:
        st.info("No audio files have been analyzed yet.")
        return

    s1, s2, s3, s4, s5 = st.columns(5)

    s1.metric("Prediction", result.get("prediction", "N/A"))
    s2.metric("Risk Level", result.get("risk_level", "N/A"))
    s3.metric("Confidence", f'{result.get("confidence", 0):.2f}%')
    s4.metric("Analysis Time", f'{result.get("processing_time", 0):.2f} sec')
    s5.metric("Audio Duration", f'{result.get("duration", 0):.2f} sec')