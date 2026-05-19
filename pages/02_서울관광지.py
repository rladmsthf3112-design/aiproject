# Streamlit 서울 관광 지도 앱

아래 내용을 각각 파일로 저장하면 Streamlit Cloud에서 바로 실행할 수 있습니다.

---

# app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🗺️ 외국인들이 좋아하는 서울 주요 관광지 TOP10")
st.markdown("폴리움(Folium) 기반 서울 관광 지도")

# 관광지 데이터
spots = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "station": "경복궁역 (3호선)",
        "fun": "한복 체험과 궁궐 산책으로 유명한 서울 대표 관광지"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.982893,
        "station": "명동역 (4호선)",
        "fun": "쇼핑, 길거리 음식, K-뷰티를 즐길 수 있는 인기 지역"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "station": "명동역 (4호선)",
        "fun": "서울 야경과 사랑의 자물쇠 명소로 유명"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "station": "안국역 (3호선)",
        "fun": "전통 한옥 거리와 감성 카페를 즐길 수 있음"
    },
    {
        "name": "홍대거리",
        "lat": 37.556327,
        "lon": 126.922996,
        "station": "홍대입구역 (2호선)",
        "fun": "버스킹, 맛집, 클럽 문화로 유명한 젊음의 거리"
    }
```
