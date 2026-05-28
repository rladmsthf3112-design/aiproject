import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="국가별 MBTI 분석",
    page_icon="🌏",
    layout="wide"
)

st.title("🌏 국가별 MBTI 분포 분석")

# ---------------------------
# 데이터 불러오기
# ---------------------------

FILE_NAME = "countriesMBTI_16types.csv"

if os.path.exists(FILE_NAME):
    df = pd.read_csv(FILE_NAME)
else:
    uploaded_file = st.file_uploader(
        "CSV 파일 업로드",
        type=["csv"]
    )

    if uploaded_file is None:
        st.stop()

    df = pd.read_csv(uploaded_file)

# ---------------------------
# 국가 컬럼 찾기
# ---------------------------

country_col = df.columns[0]

mbti_cols = [
    col for col in df.columns
    if col != country_col
]

# ---------------------------
# 국가 선택
# ---------------------------

country = st.selectbox(
    "국가 선택",
    sorted(df[country_col].unique())
)

selected = df[df[country_col] == country].iloc[0]

mbti_data = pd.DataFrame({
    "MBTI": mbti_cols,
    "비율": [selected[col] for col in mbti_cols]
})

mbti_data = mbti_data.sort_values(
    "비율",
    ascending=False
).reset_index(drop=True)

# ---------------------------
# 색상 생성
# ---------------------------

colors = []

for i in range(len(mbti_data)):

    if i == 0:
        # 1등은 핑크
        colors.append("#FF69B4")

    else:
        # 초록 그라데이션
        alpha = 0.25 + (i / len(mbti_data)) * 0.75

        green = f"rgba(46, 204, 113, {alpha})"

        colors.append(green)

# ---------------------------
# 그래프
# ---------------------------

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_data["MBTI"],
        y=mbti_data["비율"],
        marker_color=colors,
        text=[
            f"{v:.2%}" if v <= 1 else f"{v:.2f}%"
            for v in mbti_data["비율"]
        ],
        textposition="outside"
    )
)

fig.update_layout(
    title=f"{country} MBTI 분포",
    height=650,
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------
# TOP 5 표시
# ---------------------------

st.subheader("🏆 TOP 5 MBTI")

top5 = mbti_data.head(5)

for idx, row in top5.iterrows():
    st.write(
        f"{idx+1}. {row['MBTI']} : {row['비율']:.2f}%"
    )

# ---------------------------
# 전체 데이터 보기
# ---------------------------

with st.expander("전체 MBTI 비율 보기"):
    st.dataframe(
        mbti_data,
        use_container_width=True
    )
