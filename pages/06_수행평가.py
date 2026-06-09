import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="지역별 탈북민 현황",
    page_icon="📊",
    layout="wide"
)

st.title("📊 우리나라 지역별 탈북민 거주 현황")

uploaded_file = st.file_uploader(
    "CSV 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df = df.sort_values(
        by="인원수",
        ascending=False
    ).reset_index(drop=True)

    df["순위"] = range(1, len(df) + 1)

    colors = []

    for rank in df["순위"]:

        if rank == 1:
            colors.append("#FF69B4")  # 핑크

        elif rank == 2:
            colors.append("#1E90FF")  # 파랑

        elif rank == 3:
            colors.append("#32CD32")  # 초록

        else:
            colors.append("#B0B0B0")  # 회색

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["지역"],
            y=df["인원수"],
            mode="lines+markers+text",
            text=df["순위"].astype(str) + "위",
            textposition="top center",
            marker=dict(
                size=16,
                color=colors
            ),
            line=dict(
                color="#808080",
                width=3
            )
        )
    )

    fig.update_layout(
        title="지역별 탈북민 거주 인원 순위",
        xaxis_title="지역",
        yaxis_title="탈북민 수",
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🏆 TOP 10")

    st.dataframe(
        df[["순위", "지역", "인원수"]],
        use_container_width=True
    )

else:
    st.info("지역, 인원수 컬럼이 있는 CSV 파일을 업로드하세요.")
