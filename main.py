import streamlit as st  # <-- 이 줄이 빠지면 NameError가 발생합니다!
try:
    from youtubesearchpython import VideosSearch
except ImportError:
    st.error("라이브러리가 부족해요! requirements.txt에 'youtube-search-python'을 추가해주세요.")

import time

# 1. 페이지 설정
st.set_page_config(page_title="AI Level-Up Shop", page_icon="🍭", layout="wide")

# 2. 디자인 스타일
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F2; }
    .level-card { padding: 20px; border-radius: 25px; margin-bottom: 25px; }
    .beginner { background-color: #E3F2FD; border: 3px solid #90CAF9; }
    .intermediate { background-color: #FFF3E0; border: 3px solid #FFCC80; }
    .advanced { background-color: #F3E5F5; border: 3px solid #CE93D8; }
    </style>
    """, unsafe_allow_html=True)

# 3. 실시간 영상 검색 함수
def get_video(tool_name):
    try:
        search = VideosSearch(f"{tool_name} 사용법 꿀팁 가이드", limit=1)
        res = search.result()['result'][0]
        return res['link'], res['title']
    except:
        return "https://www.youtube.com/watch?v=0pL07P0U7P0", "추천 영상을 불러올 수 없어요"

# 4. 데이터셋
ai_levels = {
    "🌱 입문 캔디": {"class": "beginner", "tools": ["ChatGPT", "Canva", "Luma AI"]},
    "🌿 중급 젤리": {"class": "intermediate", "tools": ["Perplexity", "Gamma", "Notion AI"]},
    "🔥 고수 초콜릿": {"class": "advanced", "tools": ["Cursor AI", "Runway", "ElevenLabs"]}
}

# 5. UI 메인
st.title("🍭 AI Level-Up Candy Shop")
st.write("나의 숙련도에 맞는 AI 도구와 실시간 추천 영상을 확인하세요!")

selected_level = st.radio("✨ 현재 나의 레벨은?", list(ai_levels.keys()), horizontal=True)
level_data = ai_levels[selected_level]

st.markdown(f'<div class="{level_data["class"]} level-card">', unsafe_allow_html=True)
selected_tool = st.selectbox("🎯 궁금한 도구를 선택하세요", level_data["tools"])

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader(f"✨ {selected_tool} 마스터 비법")
    st.write("1. **구체적인 목표**를 정하고 질문하세요.")
    st.write("2. AI가 준 답변에 **꼬리 질문**을 던져보세요.")
    st.link_button(f"{selected_tool} 바로가기 ✈️", "https://google.com")

with col2:
    with st.spinner("GPT가 최적의 영상을 찾는 중..."):
        v_url, v_title = get_video(selected_tool)
        st.write(f"📺 **추천 영상:** {v_title}")
        st.video(v_url)

st.markdown('</div>', unsafe_allow_html=True)
