st.divider()

st.header("🌎 MBTI 유형별 TOP 10 국가")

selected_mbti = st.selectbox(
    "MBTI 유형 선택",
    mbti_cols,
    key="top10_mbti"
)

# 숫자형으로 변환
temp_df = df.copy()
temp_df[selected_mbti] = pd.to_numeric(
    temp_df[selected_mbti],
    errors="coerce"
)

top10 = (
    temp_df[[country_col, selected_mbti]]
    .dropna()
    .sort_values(by=selected_mbti, ascending=False)
    .head(10)
)

# 색상
colors = []

for i in range(len(top10)):
    if i == 0:
        colors.append("#FF69B4")  # 1위 핑크
    else:
        opacity = max(0.25, 1 - (i * 0.08))
        colors.append(f"rgba(46,204,113,{opacity})")

# 가로 막대그래프 추천
fig_top10 = go.Figure(
    go.Bar(
        x=top10[selected_mbti],
        y=top10[country_col],
        orientation="h",
        marker_color=colors,
        text=[f"{v:.2f}%" for v in top10[selected_mbti]],
        textposition="outside"
    )
)

fig_top10.update_layout(
    title=f"{selected_mbti} 비율이 가장 높은 국가 TOP 10",
    xaxis_title="비율 (%)",
    yaxis_title="국가",
    height=650,
    showlegend=False,
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(
    fig_top10,
    use_container_width=True
)

st.dataframe(
    top10.rename(
        columns={
            country_col: "국가",
            selected_mbti: "비율(%)"
        }
    ),
    use_container_width=True
)
