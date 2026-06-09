import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="지역별 강수량 분석",
    page_icon="🌧️",
    layout="wide"
)

st.title("🌧️ 지역별 강수량 분석")

# 파일 읽기
df = pd.read_csv(
    "eunseo.csv",
    encoding="cp949"
)

# 강수량 숫자 변환
df["강수량(mm)"] = pd.to_numeric(
    df["강수량(mm)"],
    errors="coerce"
)

# 결측 제거
df = df.dropna(subset=["강수량(mm)"])

# 상위 20개만 표시
df = (
    df.sort_values(
        by="강수량(mm)",
        ascending=False
    )
    .head(20)
    .reset_index(drop=True)
)

# 순위 생성
df["순위"] = range(1, len(df) + 1)

# 색상 지정
colors = []

for rank in df["순위"]:

    if rank == 1:
        colors.append("#FF69B4")

    elif rank == 2:
        colors.append("#1E90FF")

    elif rank == 3:
        colors.append("#32CD32")

    else:
        colors.append("#B0B0B0")

# 그래프
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["표준유역"],
        y=df["강수량(mm)"],
        mode="lines+markers+text",
        text=df["순위"].astype(str) + "위",
        textposition="top center",
        marker=dict(
            size=14,
            color=colors
        ),
        line=dict(
            color="#808080",
            width=3
        )
    )
)

fig.update_layout(
    title="강수량 상위 20개 유역",
    xaxis_title="유역",
    yaxis_title="강수량(mm)",
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📋 강수량 순위")

st.dataframe(
    df[
        ["순위", "표준유역", "강수량(mm)"]
    ],
    use_container_width=True
)
