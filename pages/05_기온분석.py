# 월 선택
month = st.selectbox(
    "월 선택",
    range(1, 13),
    index=7
)

# 일 선택
day = st.selectbox(
    "일 선택",
    range(1, 32),
    index=14
)

# 월, 일 추출
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day
df["연도"] = df["날짜"].dt.year

filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
].sort_values("연도")

if filtered.empty:
    st.warning("데이터가 없습니다.")
    st.stop()
