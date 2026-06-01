import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 인구 연령 분석",
    layout="wide"
)

st.title("📊 서울시 행정구별 연령 인구 분석")

uploaded_file = st.file_uploader(
    "population.csv 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file, encoding="cp949")

    district_col = df.columns[0]

    age_columns = [
        col for col in df.columns
        if "세" in col and "총인구수" not in col
    ]

    districts = df[district_col].tolist()

    selected_district = st.selectbox(
        "행정구 선택",
        districts
    )

    row = df[df[district_col] == selected_district].iloc[0]

    ages = []
    populations = []

    for col in age_columns:

        age_name = col.split("_")[-1]

        try:
            value = str(row[col]).replace(",", "")
            populations.append(int(value))
            ages.append(age_name)
        except:
            pass

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ages,
            y=populations,
            mode="lines+markers",
            line=dict(
                color="yellow",
                width=4
            ),
            marker=dict(
                size=8,
                color="yellow"
            ),
            name="인구수"
        )
    )

    fig.update_layout(
        title=f"{selected_district} 연령별 인구",
        xaxis_title="나이",
        yaxis_title="인구수",
        plot_bgcolor="#f2f2f2",
        paper_bgcolor="#f2f2f2",
        height=600,
        font=dict(size=14)
    )

    fig.update_xaxes(
        showgrid=False
    )

    fig.update_yaxes(
        gridcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
