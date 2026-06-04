import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(
page_title="서울 기온 분석 및 예측",
page_icon="🌡️",
layout="wide"
)

st.title("🌡️ 서울 기온 분석 및 미래 예측")

@st.cache_data
def load_data():

```
encodings = ["cp949", "euc-kr", "utf-8"]

for enc in encodings:
    try:
        df = pd.read_csv("seoul.csv", encoding=enc)
        break
    except:
        continue

df.columns = df.columns.str.strip()

df["날짜"] = pd.to_datetime(
    df["날짜"],
    errors="coerce"
)

df = df.dropna(subset=["날짜"])

df = df.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day

return df
```

df = load_data()

st.sidebar.header("조건 선택")

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

st.subheader(f"📈 {month}월 {day}일 기온 변화")

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
"예측할 연도",
min_value=int(df["연도"].max()) + 1,
max_value=2100,
value=2030
)

X = filtered[["연도"]]

y_max = filtered["최고기온(℃)"]
y_min = filtered["최저기온(℃)"]

max_model = LinearRegression()
min_model = LinearRegression()

max_model.fit(X, y_max)
min_model.fit(X, y_min)

future = np.array([[future_year]])

pred_max = max_model.predict(future)[0]
pred_min = min_model.predict(future)[0]

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
"예측값은 과거 데이터를 이용한 선형회귀 결과이며 실제 기온과 차이가 있을 수 있습니다."
)
