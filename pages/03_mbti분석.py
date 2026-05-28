import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="국가별 MBTI 분석",
    page_icon="🌎",
    layout="wide"
)

st.title("🌎 국가별 MBTI 국가 분석")

# -----------------------
# 데이터 불러오기
# -----------------------

df = pd.read_csv("countriesMBTI_16types.csv")

# 첫 번째 컬럼 = 국가명
country_col = df.columns[0]

# MBTI 컬럼
mbti_cols = [
    col for col in df.columns
    if col != country_col
]

# 숫자형 변환
for col in mbti_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================
# 국가별 MBTI 그래프
# =========================

st.header("📊 국가별 MBTI 분포")

selected_country = st.selectbox(
    "국가 선택",
    sorted(df[country_col].unique())
)

row = df[df[country_col] == selected_country].iloc[0]

country_data = pd.DataFrame({
    "MBTI": mbti_cols,
    "비율": [row[col] for col in mbti_cols]
})

country_data = country_data.sort_values(
    "비율",
    ascending=False
).reset_index(drop=True)

# 색상
colors = []

for i in range(len(country_data)):

    if i == 0:
        colors.append("#FF69B4")

    else:
        opacity = 1 - (i * 0.05)

        if opacity < 0.2:
            opacity = 0.2

        colors.append(
            f"rgba(46,204,113,{opacity})"
        )

fig = go.Figure()

fig.add_bar(
    x=country_data["MBTI"],
    y=country_data["비율"],
    marker_color=colors,
    text=country_data["비율"].round(2),
    textposition="outside"
)

fig.update_layout(
    title=f"{selected_country} MBTI 분포",
    xaxis_title="MBTI",
    yaxis_title="비율 (%)",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# MBTI별 TOP10 국가
# =========================

st.divider()

st.header("🏆 MBTI 유형별 TOP 10 국가")

selected_mbti = st.selectbox(
    "MBTI 유형 선택",
    mbti_cols
)

top10 = (
    df[[country_col, selected_mbti]]
    .dropna()
    .sort_values(
        by=selected_mbti,
        ascending=False
    )
    .head(10)
    .reset_index(drop=True)
)

colors2 = []

for i in range(len(top10)):

    if i == 0:
        colors2.append("#FF69B4")

    else:
        opacity = 1 - (i * 0.07)

        if opacity < 0.2:
            opacity = 0.2

        colors2.append(
            f"rgba(46,204,113,{opacity})"
        )

fig2 = go.Figure()

fig2.add_bar(
    x=top10[country_col],
    y=top10[selected_mbti],
    marker_color=colors2,
    text=top10[selected_mbti].round(2),
    textposition="outside"
)

fig2.update_layout(
    title=f"{selected_mbti} 비율이 높은 국가 TOP 10",
    xaxis_title="국가",
    yaxis_title="비율 (%)",
    height=600
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.dataframe(
    top10.rename(
        columns={
            country_col: "국가",
            selected_mbti: "비율 (%)"
        }
    ),
    use_container_width=True
)
