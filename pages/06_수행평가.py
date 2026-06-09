import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="학년별 희망 직업",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 중1 ~ 고3 희망 직업 순위")

uploaded_file = st.file_uploader(
    "희망직업 CSV 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    grades = [
        "중1", "중2", "중3",
        "고1", "고2", "고3"
    ]

    grade = st.selectbox(
        "학년 선택",
        grades
    )

    grade_df = (
        df[df["학년"] == grade]
        .sort_values("순위")
    )

    marker_colors = []

    for rank in grade_df["순위"]:

        if rank == 1:
            marker_colors.append("#FF69B4")  # 핑크

        elif rank == 2:
            marker_colors.append("#1E90FF")  # 파랑

        elif rank == 3:
            marker_colors.append("#32CD32")  # 초록

        else:
            marker_colors.append("#B0B0B0")  # 회색

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=grade_df["직업"],
            y=grade_df["순위"],
            mode="lines+markers+text",
            text=grade_df["순위"],
            textposition="top center",
            marker=dict(
                size=16,
                color=marker_colors
            ),
            line=dict(
                color="#808080",
                width=3
            )
        )
    )

    fig.update_layout(
        title=f"{grade} 희망 직업 순위",
        xaxis_title="직업",
        yaxis_title="순위",
        yaxis=dict(
            autorange="reversed"
        ),
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.info("CSV 파일을 업로드하세요.")
