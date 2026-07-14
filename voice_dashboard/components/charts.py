import streamlit as st
import pandas as pd
import plotly.express as px


PREDICTION_COLORS = {
    "Real": "#22c55e",
    "Spoof Detected": "#ef4444"
}

RISK_COLORS = {
    "LOW": "#22c55e",
    "MEDIUM": "#f59e0b",
    "HIGH": "#ef4444"
}


def normalize_predictions(df):
    df = df.copy()

    df["Prediction"] = df["Prediction"].replace({
        "Genuine": "Real",
        "Fake": "Spoof Detected",
        "FAKE": "Spoof Detected",
        "REAL": "Real"
    })

    return df


def apply_clean_layout(fig):
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#111827", size=14),
        title=dict(
            font=dict(size=22, color="#0f172a"),
            x=0.02,
            xanchor="left"
        ),
        margin=dict(l=45, r=30, t=70, b=55),
        height=420
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor="#CBD5E1",
        tickfont=dict(color="#64748b", size=13),
        title_font=dict(color="#64748b", size=14)
    )

    fig.update_yaxes(
        gridcolor="#E5E7EB",
        zeroline=False,
        linecolor="#CBD5E1",
        tickfont=dict(color="#64748b", size=13),
        title_font=dict(color="#64748b", size=14)
    )

    return fig


def render_probability_chart(real_prob: float, fake_prob: float):
    st.markdown('<div class="section-title">Prediction Probabilities</div>', unsafe_allow_html=True)

    prob_df = pd.DataFrame({
        "Class": ["Real", "Spoof Detected"],
        "Probability (%)": [real_prob, fake_prob]
    })

    fig = px.bar(
        prob_df,
        x="Class",
        y="Probability (%)",
        text="Probability (%)",
        title="Current Recording Classification Probability",
        color="Class",
        color_discrete_map=PREDICTION_COLORS
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        yaxis_title="Probability (%)",
        xaxis_title="Prediction"
    )

    fig = apply_clean_layout(fig)
    st.plotly_chart(fig, use_container_width=True)


def render_database_charts(history_df):
    st.markdown('<div class="section-title">Analytics Overview</div>', unsafe_allow_html=True)

    if history_df.empty:
        st.info("No data available yet. Analyze recordings to view analytics.")
        return

    df = normalize_predictions(history_df)

    df["Confidence"] = pd.to_numeric(df["Confidence"], errors="coerce")
    df["Processing Time"] = pd.to_numeric(df["Processing Time"], errors="coerce")

    col1, col2 = st.columns(2)

    with col1:
        pie_df = df["Prediction"].value_counts().reset_index()
        pie_df.columns = ["Prediction", "Count"]

        pie_df["Label"] = (
            pie_df["Prediction"] +
            " (" +
            pie_df["Count"].astype(str) + ")"
        )

        fig_pie = px.pie(
            pie_df,
            names="Label",
            values="Count",
            title="Prediction Distribution",
            hole=0.45,
            color="Prediction",
            color_discrete_map=PREDICTION_COLORS
        )

        fig_pie.update_traces(
            textinfo="percent",
            textposition="inside",
            textfont=dict(size=16, color="white"),
            hovertemplate="<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>"
        )

        fig_pie.update_layout(
            legend_title_text="Prediction",
            margin=dict(l=30, r=30, t=70, b=80),
            height=420
        )

        fig_pie = apply_clean_layout(fig_pie)


        total = len(df)
        
        fig_pie.add_annotation(
            text=f"<b>Total Checked Recordings: {total}</b>",
            x=0.02,
            y=-0.15,
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(
                size=15,
                color="#6B7280"
                ),
            align="left"
)

        st.plotly_chart(fig_pie, use_container_width=True)


    with col2:
        avg_conf_df = (
            df.groupby("Prediction", as_index=False)["Confidence"]
            .mean()
            .round(2)
        )

        fig_conf = px.bar(
            avg_conf_df,
            x="Prediction",
            y="Confidence",
            text="Confidence",
            title="Average Confidence by Prediction",
            color="Prediction",
            color_discrete_map=PREDICTION_COLORS
        )

        fig_conf.update_traces(
            texttemplate="%{text:.2f}%",
            textposition="outside",
            cliponaxis=False
            )

        fig_conf.update_layout(
            showlegend=False,
            yaxis_title="Confidence (%)",
            xaxis_title="Prediction",
            yaxis=dict(range=[0, 115])
            )

        fig_conf = apply_clean_layout(fig_conf)

        st.plotly_chart(fig_conf, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        avg_time_df = (
            df.groupby("Prediction", as_index=False)["Processing Time"]
            .mean()
            .round(3)
        )

        fig_time = px.bar(
            avg_time_df,
            x="Prediction",
            y="Processing Time",
            text="Processing Time",
            title="Average Processing Time by Prediction",
            color="Prediction",
            color_discrete_map=PREDICTION_COLORS
        )

        fig_time.update_traces(
            texttemplate="%{text:.3f} sec",
            textposition="outside"
        )

        fig_time.update_layout(
            showlegend=False,
            yaxis_title="Processing Time (sec)",
            xaxis_title="Prediction"
        )

        fig_time = apply_clean_layout(fig_time)

        st.plotly_chart(fig_time, use_container_width=True)

    with col4:
        risk_order = ["LOW", "MEDIUM", "HIGH"]

        risk_df = df["Risk Level"].value_counts().reset_index()
        risk_df.columns = ["Risk Level", "Count"]

        risk_df["Risk Level"] = pd.Categorical(
            risk_df["Risk Level"],
            categories=risk_order,
            ordered=True
        )

        risk_df = risk_df.sort_values("Risk Level")

        fig_risk = px.bar(
            risk_df,
            x="Risk Level",
            y="Count",
            text="Count",
            title="Risk Level Distribution",
            color="Risk Level",
            color_discrete_map=RISK_COLORS
        )

        fig_risk.update_traces(
            texttemplate="%{text}",
            textposition="outside"
        )

        fig_risk.update_layout(
            showlegend=False,
            yaxis_title="Number of Recordings",
            xaxis_title="Risk Level"
        )

        fig_risk = apply_clean_layout(fig_risk)

        st.plotly_chart(fig_risk, use_container_width=True)