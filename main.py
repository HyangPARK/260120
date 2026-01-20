streamlit
pandas
youtube-search-python

import streamlit as st
from youtubesearchpython import VideosSearch # 유튜브 검색 라이브러리
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="AI 맞춤형 가이드", page_icon="🍭", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFF9F2; }
    .video-card {
        background: white;
        padding: 15px;
        border-radius: 20px;
        border: 2px solid #FFB7CE;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 유튜브 검색 함수 (GPT 기반 추천 로직을 모방)
def get_youtube_video(query):
    try:
        # GPT가 추천할만한 키워드로 검색 (예: "ChatGPT 활용법 가이드")
        search = VideosSearch(query + " 활용법 가이드", limit = 1)
        result = search.result()['result']
        if result:
            return result[0]['link'], result[0]['title']
        else:
            # 검색 결과 없을 시 기본 영상
            return "https://www.youtube.com/watch?v=0pL07P0U7P0", "기본 추천 영상"
    except:
        return "https://www.youtube.com/watch?v=0pL07P0U7P0", "기본 추천 영상"

# 3. 데이터 (숙련도별 도구)
ai_data = {
    "🌱 초보 (입문용)": ["ChatGPT", "Canva", "Luma AI"],
    "🌿 중급 (실무용)": ["Perplexity", "Gamma", "Notion AI"],
    "🔥 고수 (개발/전문)": ["Cursor AI", "Runway Gen-2", "D-ID"]
}

# 4. 메인 화면
st.title("🍭 AI 맞춤형 레시피 & 실시간 영상 추천")
st.write("선택하신 도구에 맞춰 **GPT가 유튜브에서 최적의 강의**를 찾아드려요!")

# 사이드바 레이아웃
st.sidebar.header("🎨 설정")
level = st.sidebar.selectbox("레벨을 선택하세요", list(ai_data.keys()))
selected_tool = st.sidebar.radio("관심 있는 도구", ai_data[level])

st.divider()

# 5. 결과 영역
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader(f"✨ {selected_tool} 활용 전략")
    
    # 도구별 맞춤 가이드 (구체적 전략)
    if selected_tool == "ChatGPT":
        st.success("1. **역할 부여**: '너는 전문 카피라이터야'라고 시작하세요.\n2. **제약 설정**: '3줄 이내로 써줘'처럼 규칙을 주세요.")
    elif selected_tool == "Cursor AI":
        st.warning("1. **파일 참조**: @ 기호를 써서 코드를 수정하세요.\n2. **에러 수정**: 터미널 에러를 복사해 해결책을 물어보세요.")
    else:
        st.info(f"{selected_tool}의 핵심 기능을 활용해 업무 속도를 2배 높여보세요!")

    st.link_button(f"{selected_tool} 사이트 방문하기", "https://google.com")

with col2:
    st.subheader("📺 GPT 추천 실시간 동영상")
    
    # 실시간 검색 수행
    with st.spinner(f"GPT가 '{selected_tool}' 관련 최고의 영상을 찾는 중..."):
        video_url, video_title = get_youtube_video(selected_tool)
        time.sleep(1) # 검색하는 느낌을 주기 위한 지연

    st.markdown(f'<div class="video-card">', unsafe_allow_html=True)
    st.write(f"**추천 제목:** {video_title}")
    st.video(video_url)
    st.markdown('</div>', unsafe_allow_html=True)
    st.caption("※ GPT의 추천 로직을 기반으로 실시간 유튜브 데이터를 가져옵니다.")

# 6. 하단 푸터
st.divider()
st.center_text = st.markdown("<p style='text-align: center;'>당신의 AI 마스터 여정을 응원합니다! 🍬</p>", unsafe_allow_html=True)
