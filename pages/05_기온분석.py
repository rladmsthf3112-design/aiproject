import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")
st.markdown("날짜를 선택하면 해당 날짜의 최고기온과 최저기온을 확인할 수 있습니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    # 컬럼명 공백 제거
    df.columns = df.columns.str.strip()

    # 날짜 변환
    df["날짜"] = pd.to_datetime(df["날짜"])

    return df

df = load_data()

# 결측치 제거
df = df.dropna(subset=["최고기온(℃)", "최저기온(℃)"])

# 날짜 선택
selected_date = st.date_input(
    "날짜 선택",
    value=df["날짜"].max().date(),
    min_value=df["날짜"].min().date(),
    max_value=df["날짜"].max().date()
)

# 선택된 날짜 데이터
selected_row = df[df["날짜"].dt.date == selected_date]

if len(selected_row) > 0:

    max_temp = float(selected_row["최고기온(℃)"].iloc[0])
    min_temp = float(selected_row["최저기온(℃)"].iloc[0])

    col1, col2 = st.columns(2)

    with col1:
        st.metric("최고기온", f"{max_temp:.1f} ℃")

    with col2:
        st.metric("최저기온", f"{min_temp:.1f} ℃")

    # 그래프
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=["최저기온", "최고기온"],
            y=[min_temp, max_temp],
            mode="lines+markers",
            name="최고기온",
            line=dict(color="hotpink", width=4),
            marker=dict(size=10, color="hotpink")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=["최저기온", "최고기온"],
            y=[min_temp, min_temp],
            mode="lines+markers",
            name="최저기온",
            line=dict(color="lightskyblue", width=4),
            marker=dict(size=10, color="lightskyblue")
        )
    )

    fig.update_layout(
        title=f"{selected_date} 기온 정보",
        xaxis_title="구분",
        yaxis_title="기온 (℃)",
        template="plotly_white",
        legend_title="범례",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("선택한 날짜의 데이터가 없습니다.")

# 데이터 보기
with st.expander("원본 데이터 보기"):
    st.dataframe(df)
