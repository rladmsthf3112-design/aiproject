import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")

@st.cache_data
def load_data():

    # 인코딩 자동 처리
    encodings = ["cp949", "euc-kr", "utf-8"]

    for enc in encodings:
        try:
            df = pd.read_csv("seoul.csv", encoding=enc)
            break
        except:
            continue

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 변환 (오류 방지)
    df["날짜"] = pd.to_datetime(
        df["날짜"],
        errors="coerce"
    )

    # 날짜 없는 행 제거
    df = df.dropna(subset=["날짜"])

    # 기온 결측 제거
    df = df.dropna(
        subset=["최고기온(℃)", "최저기온(℃)"]
    )

    return df


df = load_data()

# 날짜 선택
selected_date = st.date_input(
    "날짜 선택",
    value=df["날짜"].max().date(),
    min_value=df["날짜"].min().date(),
    max_value=df["날짜"].max().date()
)

# 선택 날짜 찾기
selected = df[df["날짜"].dt.date == selected_date]

if len(selected) == 0:
    st.warning("선택한 날짜의 데이터가 없습니다.")
    st.stop()

max_temp = float(selected["최고기온(℃)"].iloc[0])
min_temp = float(selected["최저기온(℃)"].iloc[0])

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "최고기온",
        f"{max_temp:.1f} ℃"
    )

with col2:
    st.metric(
        "최저기온",
        f"{min_temp:.1f} ℃"
    )

# 그래프용 데이터
graph_df = pd.DataFrame({
    "구분": ["최저기온", "최고기온"],
    "온도": [min_temp, max_temp]
})

fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=graph_df["구분"],
        y=[max_temp, max_temp],
        mode="lines+markers",
        name="최고기온",
        line=dict(
            color="hotpink",
            width=4
        ),
        marker=dict(size=10)
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=graph_df["구분"],
        y=[min_temp, min_temp],
        mode="lines+markers",
        name="최저기온",
        line=dict(
            color="lightskyblue",
            width=4
        ),
        marker=dict(size=10)
    )
)

fig.update_layout(
    title=f"{selected_date} 기온 정보",
    xaxis_title="구분",
    yaxis_title="기온(℃)",
    template="plotly_white",
    height=600,
    legend_title="범례"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

with st.expander("원본 데이터 보기"):
    st.dataframe(df)
