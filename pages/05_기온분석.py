import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석 및 미래 예측")

@st.cache_data
def load_data():

    df = None

    for enc in ["cp949", "euc-kr", "utf-8"]:
        try:
            df = pd.read_csv("seoul.csv", encoding=enc)
            break
        except:
            pass

    if df is None:
        st.error("seoul.csv 파일을 읽을 수 없습니다.")
        st.stop()

    df.columns = df.columns.str.strip()

    required_cols = ["날짜", "최고기온(℃)", "최저기온(℃)"]

    for col in required_cols:
        if col not in df.columns:
            st.error(f"컬럼 '{col}' 이 존재하지 않습니다.")
            st.write("현재 컬럼:", list(df.columns))
            st.stop()

    df["날짜"] = pd.to_datetime(
        df["날짜"],
        errors="coerce"
    )

    df = df.dropna(subset=["날짜"])

    df["최고기온(℃)"] = pd.to_numeric(
        df["최고기온(℃)"],
        errors="coerce"
    )

    df["최저기온(℃)"] = pd.to_numeric(
        df["최저기온(℃)"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["최고기온(℃)", "최저기온(℃)"]
    )

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df


df = load_data()

st.sidebar.header("날짜 선택")

month = st.sidebar.selectbox(
    "월",
    list(range(1, 13))
)

day = st.sidebar.selectbox(
    "일",
    list(range(1, 32))
)

filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].copy()

if filtered.empty:
    st.warning("해당 날짜 데이터가 없습니다.")
    st.stop()

filtered = filtered.sort_values("연도")

st.subheader(f"{month}월 {day}일 역대 기온 변화")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered["최고기온(℃)"],
        mode="lines",
        name="최고기온",
        line=dict(
            color="hotpink",
            width=3
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered["연도"],
        y=filtered["최저기온(℃)"],
        mode="lines",
        name="최저기온",
        line=dict(
            color="lightskyblue",
            width=3
        )
    )
)

fig.update_layout(
    template="plotly_white",
    height=600,
    legend_title="범례",
    xaxis_title="연도",
    yaxis_title="기온(℃)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("🔮 미래 기온 예측")

future_year = st.number_input(
    "예측 연도",
    min_value=int(df["연도"].max()) + 1,
    max_value=2100,
    value=2030,
    step=1
)

X = filtered[["연도"]]

max_model = LinearRegression()
min_model = LinearRegression()

max_model.fit(
    X,
    filtered["최고기온(℃)"]
)

min_model.fit(
    X,
    filtered["최저기온(℃)"]
)

pred_max = max_model.predict([[future_year]])[0]
pred_min = min_model.predict([[future_year]])[0]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "예측 최고기온",
        f"{pred_max:.1f} ℃"
    )

with col2:
    st.metric(
        "예측 최저기온",
        f"{pred_min:.1f} ℃"
    )

st.info(
    "예측값은 선택한 월·일의 과거 데이터를 기반으로 한 선형회귀 결과입니다."
)
