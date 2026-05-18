import streamlit as st

st.set_page_config(
    page_title="✨ MBTI 진로 추천기",
    page_icon="🌈",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_jobs = {
    "INTJ": [
        {
            "job": "🧠 데이터 분석가",
            "major": "데이터사이언스학과, 통계학과",
            "personality": "논리적이고 계획 세우는 걸 좋아하는 사람!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "💻 소프트웨어 개발자",
            "major": "컴퓨터공학과",
            "personality": "혼자 집중하는 걸 좋아하고 문제 해결을 즐기는 성격!",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "INTP": [
        {
            "job": "🔬 연구원",
            "major": "자연과학계열",
            "personality": "호기심 많고 새로운 아이디어를 좋아하는 사람!",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "🖥️ 프로그래머",
            "major": "컴퓨터공학과",
            "personality": "분석적이고 창의적인 성격!",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],

    "ENTJ": [
        {
            "job": "📈 마케팅 기획자",
            "major": "경영학과, 광고홍보학과",
            "personality": "리더십 있고 추진력이 강한 사람!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🏢 CEO / 창업가",
            "major": "경영학과",
            "personality": "목표 지향적이고 도전 정신이 강한 성격!",
            "salary": "평균 연봉 매우 다양함 💰"
        }
    ],

    "ENTP": [
        {
            "job": "🎤 콘텐츠 크리에이터",
            "major": "미디어학과",
            "personality": "아이디어가 많고 사람들과 소통을 좋아하는 성격!",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "📢 광고 기획자",
            "major": "광고홍보학과",
            "personality": "창의적이고 트렌드에 민감한 사람!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "INFJ": [
        {
            "job": "💖 심리상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 배려심 많은 성격!",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "📚 작가",
            "major": "문예창작학과",
            "personality": "상상력이 풍부하고 감수성이 깊은 사람!",
            "salary": "수입 차이가 큼 ✍️"
        }
    ],

    "INFP": [
        {
            "job": "🎨 디자이너",
            "major": "시각디자인학과",
            "personality": "감성적이고 창의력이 풍부한 성격!",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "📖 웹소설 작가",
            "major": "문예창작학과",
            "personality": "상상력이 뛰어나고 자유로운 사람!",
            "salary": "인기에 따라 다양함 🌟"
        }
    ],

    "ENFJ": [
        {
            "job": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 걸 좋아하고 친절한 성격!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🧑‍💼 인사담당자",
            "major": "경영학과",
            "personality": "사람 관계를 중요하게 생각하는 사람!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ENFP": [
        {
            "job": "🎬 방송인",
            "major": "방송연예과",
            "personality": "에너지 넘치고 표현력이 좋은 사람!",
            "salary": "수입 차이 큼 📺"
        },
        {
            "job": "✈️ 여행 기획자",
            "major": "관광경영학과",
            "personality": "새로운 경험을 좋아하는 자유로운 성격!",
            "salary": "평균 연봉 약 3,600만원"
        }
    ],

    "ISTJ": [
        {
            "job": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감이 강한 성격!",
            "salary": "평균 연봉 약 6,000만원"
        },
        {
            "job": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "안정적이고 성실한 사람!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ISFJ": [
        {
            "job": "🩺 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 책임감 있는 성격!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🏫 유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 참을성 있는 사람!",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESTJ": [
        {
            "job": "📋 경영 관리자",
            "major": "경영학과",
            "personality": "체계적이고 리더십 있는 성격!",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "책임감 강하고 원칙을 중요하게 생각하는 사람!",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],

    "ESFJ": [
        {
            "job": "💄 뷰티 컨설턴트",
            "major": "뷰티미용학과",
            "personality": "친절하고 사람 만나는 걸 좋아하는 성격!",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "🎉 이벤트 플래너",
            "major": "호텔관광학과",
            "personality": "분위기를 잘 이끌고 사교적인 사람!",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],

    "ISTP": [
        {
            "job": "🔧 자동차 엔지니어",
            "major": "기계공학과",
            "personality": "손재주 좋고 현실적인 성격!",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "🎮 게임 개발자",
            "major": "게임공학과",
            "personality": "문제 해결 능력이 뛰어난 사람!",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],

    "ISFP": [
        {
            "job": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 성격!",
            "salary": "수입 차이 큼 📷"
        },
        {
            "job": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "예술 감각이 뛰어난 사람!",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],

    "ESTP": [
        {
            "job": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "말 잘하고 활동적인 성격!",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "🚓 스포츠 트레이너",
            "major": "체육학과",
            "personality": "에너지 넘치고 행동력이 좋은 사람!",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],

    "ESFP": [
        {
            "job": "🎤 연예인 / 배우",
            "major": "연극영화과",
            "personality": "사람들 앞에 서는 걸 좋아하는 성격!",
            "salary": "수입 차이 매우 큼 🌟"
        },
        {
            "job": "🍰 파티셰",
            "major": "제과제빵학과",
            "personality": "감각적이고 밝은 사람!",
            "salary": "평균 연봉 약 3,300만원"
        }
    ]
}

# 제목
st.title("🌈 MBTI 진로 추천기")
st.write("내 MBTI에 어울리는 직업이 궁금하다면?! 😎")
st.write("아래에서 MBTI를 선택해봐 ✨")

# 선택 박스
selected_mbti = st.selectbox(
    "🔍 MBTI 선택하기",
    list(mbti_jobs.keys())
)

# 결과 출력
if selected_mbti:
    st.header(f"💖 {selected_mbti} 추천 진로")

    jobs = mbti_jobs[selected_mbti]

    for job in jobs:
        st.subheader(job["job"])

        st.write(f"📚 추천 학과: {job['major']}")
        st.write(f"🧩 어울리는 성격: {job['personality']}")
        st.write(f"💰 평균 연봉: {job['salary']}")

        st.markdown("---")

st.caption("✨ 재미로 보는 추천이니까 너무 진지하게만 보진 말기! 😆")
