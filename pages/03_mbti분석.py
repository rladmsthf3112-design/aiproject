st.divider()

st.header("🌎 MBTI 유형별 TOP 10 국가")

selected_mbti = st.selectbox(
    "MBTI 유형 선택",
    mbti_cols
)

top10 = (
    df[[country_col, selected_mbti]]
    .sort_values(selected_mbti, ascending=False)
    .head(10)
)

colors = []

for i in range(len(top10)):
    if i == 0:
        colors.append("#FF69B4")  # 1위 핑크
    else:
        alpha = 0.3 + (i / 10) * 0.7
        colors.append(f"rgba(46,204,113,{alpha})")

fig_top10 = go.Figure()

fig_top10.add_trace(
    go.Bar(
        x=top10[country_col],
        y=top10[selected_mbti],
        marker_color=colors,
        text=[f"{v:.2f}%" for v in top10[selected_mbti]],
        textposition="outside"
    )
)

fig_top10.update_layout(
    title=f"{selected_mbti} 비율이 가장 높은 국가 TOP 10",
    xaxis_title="국가",
    yaxis_title="비율 (%)",
    height=600,
    showlegend=False
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
