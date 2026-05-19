import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 추천봇 📚🎬",
    page_icon="✨",
    layout="centered"
)

# 제목
st.title("✨ MBTI 책 & 영화 추천기 🎬")
st.write("너의 MBTI에 맞는 감성 작품들을 추천해줄게 😎")

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "book_old": ("1984", "조지 오웰"),
        "book_new": ("사피엔스", "유발 하라리"),
        "movies": ["시민 케인", "대부"]
    },
    "INTP": {
        "book_old": ("데미안", "헤르만 헤세"),
        "book_new": ("코스모스", "칼 세이건"),
        "movies": ["카사블랑카", "록키"]
    },
    "ENTJ": {
        "book_old": ("군주론", "마키아벨리"),
        "book_new": ("넛지", "리처드 탈러"),
        "movies": ["죠스", "스타워즈"]
    },
    "ENTP": {
        "book_old": ("멋진 신세계", "올더스 헉슬리"),
        "book_new": ("팩트풀니스", "한스 로슬링"),
        "movies": ["택시 드라이버", "대탈주"]
    },
    "INFJ": {
        "book_old": ("어린 왕자", "생텍쥐페리"),
        "book_new": ("연금술사", "파울로 코엘료"),
        "movies": ["사운드 오브 뮤직", "로마의 휴일"]
    },
    "INFP": {
        "book_old": ("노인과 바다", "헤밍웨이"),
        "book_new": ("채식주의자", "한강"),
        "movies": ["티파니에서 아침을", "바람과 함께 사라지다"]
    },
    "ENFJ": {
        "book_old": ("오만과 편견", "제인 오스틴"),
        "book_new": ("미움받을 용기", "기시미 이치로"),
        "movies": ["록키", "사랑은 비를 타고"]
    },
    "ENFP": {
        "book_old": ("호밀밭의 파수꾼", "샐린저"),
        "book_new": ("달러구트 꿈 백화점", "이미예"),
        "movies": ["그리스", "죠스"]
    },
    "ISTJ": {
        "book_old": ("죄와 벌", "도스토예프스키"),
        "book_new": ("아몬드", "손원평"),
        "movies": ["12인의 성난 사람들", "록키"]
    },
    "ISFJ": {
        "book_old": ("작은 아씨들", "올컷"),
        "book_new": ("불편한 편의점", "김호연"),
        "movies": ["사브리나", "사운드 오브 뮤직"]
    },
    "ESTJ": {
        "book_old": ("인간 실격", "다자이 오사무"),
        "book_new": ("부의 추월차선", "엠제이 드마코"),
        "movies": ["스타워즈", "대부"]
    },
    "ESFJ": {
        "book_old": ("위대한 개츠비", "피츠제럴드"),
        "book_new": ("완득이", "김려령"),
        "movies": ["카사블랑카", "로마의 휴일"]
    },
    "ISTP": {
        "book_old": ("노인과 바다", "헤밍웨이"),
        "book_new": ("트렌드 코리아", "김난도"),
        "movies": ["대탈주", "죠스"]
    },
    "ISFP": {
        "book_old": ("이방인", "카뮈"),
        "book_new": ("소년이 온다", "한강"),
        "movies": ["티파니에서 아침을", "사브리나"]
    },
    "ESTP": {
        "book_old": ("해리포터", "J.K. 롤링"),
        "book_new": ("파친코", "이민진"),
        "movies": ["록키", "스타워즈"]
    },
    "ESFP": {
        "book_old": ("위대한 개츠비", "피츠제럴드"),
        "book_new": ("아가미", "구병모"),
        "movies": ["그리스", "죠스"]
    }
}

# MBTI 선택
selected_mbti = st.selectbox(
    "👉 너의 MBTI를 선택해봐!",
    list(mbti_data.keys())
)

# 결과 출력
if selected_mbti:
    data = mbti_data[selected_mbti]

    st.markdown("---")
    st.header(f"💖 {selected_mbti} 추천 결과!")

    st.subheader("📚 책 추천")

    st.write("🕰️ 1900년대 작가 책")
    st.success(f"『{data['book_old'][0]}』 - {data['book_old'][1]}")

    st.write("🚀 2000년대 이후 작가 책")
    st.success(f"『{data['book_new'][0]}』 - {data['book_new'][1]}")

    st.subheader("🎬 영화 추천")
    st.write("🍿 1980년대 이전 미국 영화 추천!")

    for movie in data["movies"]:
        st.info(f"🎞️ {movie}")

    st.markdown("---")
    st.write("✨ 재밌게 봤다면 친구한테도 공유해봐 😆")
