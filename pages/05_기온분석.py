import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def load_data():

    # 인코딩 자동 시도
    for enc in ["cp949", "euc-kr", "utf-8"]:
        try:
            df = pd.read_csv("seoul.csv", encoding=enc)
            break
        except:
            pass

    df.columns = df.columns.str.strip()

    # 실제 컬럼명 확인용
    st.write("컬럼명:", df.columns.tolist())

    # 날짜 변환
    df["날짜"] = pd.to_datetime(df["날짜"], errors="coerce")

    df = df.dropna(subset=["날짜"])

    return df

df = load_data()

# 월, 일 컬럼 생성
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day
df["연도"] = df["날짜"].dt.year

month = st.selectbox("월 선택", list(range(1, 13)))
day = st.selectbox("일 선택", list(range(1, 32)))

filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
]

if filtered.empty:
    st.warning("해당 날짜 데이터가 없습니다.")
else:

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=filtered["연도"],
            y=filtered["최고기온(℃)"],
            mode="lines",
            name="최고기온",
            line=dict(color="hotpink", width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=filtered["연도"],
            y=filtered["최저기온(℃)"],
            mode="lines",
            name="최저기온",
            line=dict(color="lightskyblue", width=3)
        )
    )

    fig.update_layout(
        title=f"{month}월 {day}일 기온 변화",
        xaxis_title="연도",
        yaxis_title="기온(℃)",
        legend_title="범례",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
