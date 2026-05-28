st.divider()

st.header("🌎 MBTI 유형별 TOP 10 국가")

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI 유형 선택",
    mbti_cols,
    key="top10"
)

# 국가 컬럼 + MBTI 컬럼만 추출
top10 = df[[country_col, selected_mbti]].copy()

# 숫자로 변환
top10[selected_mbti] = pd.to_numeric(
    top10[selected_mbti],
    errors="coerce"
)

# 결측 제거
top10 = top10.dropna()

# 정렬
top10 = top10.sort_values(
    by=selected_mbti,
    ascending=False
).head(10)

# 색상
colors = ["#FF69B4"]

for i in range(1, len(top10)):
    opacity = 1 - (i * 0.08)

    if opacity < 0.25:
        opacity = 0.25

    colors.append(
        f"rgba(46,204,113,{opacity})"
    )

# 그래프
fig_top10 = go.Figure()

fig_top10.add_bar(
    x=top10[country_col],
    y=top10[selected_mbti],
    marker_color=colors,
    text=top10[selected_mbti].round(2),
    textposition="outside"
)

fig_top10.update_layout(
    title=f"{selected_mbti} 비율 TOP 10 국가",
    xaxis_title="국가",
    yaxis_title="비율",
    height=600
)

st.plotly_chart(
    fig_top10,
    use_container_width=True
)
