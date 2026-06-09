import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="년도별 재난 발생 현황",
    page_icon="📈",
    layout="wide"
)

st.title("📈 년도별 재난 발생 현황")

uploaded_file = st.file_uploader(
    "재난 데이터 CSV 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df["년도"] = pd.to_numeric(df["년도"], errors="coerce")
    df["재난건수"] = pd.to_numeric(df["재난건수"], errors="coerce")

    df = df.sort_values("년도")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["년도"],
            y=df["재난건수"],
            mode="lines+markers+text",
            text=df["재난건수"],
            textposition="top center",
            line=dict(
                color="#1E90FF",
                width=4
            ),
            marker=dict(
                size=10
            )
        )
    )

    fig.update_layout(
        title="년도별 재난 발생 건수",
        xaxis_title="년도",
        yaxis_title="재난 건수",
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("📋 데이터")

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("년도, 재난건수 컬럼이 포함된 CSV 파일을 업로드하세요.")
