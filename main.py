import streamlit as st

# 1. 캔디샵 느낌의 페이지 설정
st.set_page_config(page_title="AI Candy Shop", page_icon="🍬", layout="wide")

# 2. 귀여움을 한스푼 넣은 CSS 커스텀
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Nanum Gothic', sans-serif;
        background-color: #FFF5F7; /* 연한 핑크 배경 */
    }
    .stButton>button {
        background-color: #FFB7CE;
        color: white;
        border-radius: 50px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF8FAB;
        transform: scale(1.05);
    }
    .strategy-card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        border: 3px dashed #FFB7CE;
        margin-bottom: 20px;
    }
    .step-box {
        background-color: #F0F2FF;
        padding: 10px 15px;
        border-left: 5px solid #6C63FF;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 메인 타이틀
st.title("🍬 AI Candy Shop")
st.subheader("한 번 먹으면 멈출 수 없는 달콤한 AI 활용 레시피! 🍰")
st.write("---")

# 4. AI 도구별 구체적인 '시크릿 레시피' 데이터
recipes = {
    "✍️ 글쓰기 요정 (ChatGPT)": {
        "intro": "복잡한 고민을 사르르 녹여주는 만능 요정이에요!",
        "strategy": [
            "**Step 1. 페르소나 입히기**: '너는 10년 차 베테랑 마케터야'라고 역할을 정해주세요.",
            "**Step 2. 구체적인 재료 넣기**: 단순히 '글 써줘' 말고, '타겟은 20대, 말투는 다정하게, 글자 수는 500자로!'라고 주문하세요.",
            "**Step 3. 피드백으로 간 맞추기**: 결과가 나오면 '조금 더 재미있게 수정해줘!'라고 추가 주문을 해보세요."
        ],
        "prompt_example": "📍 **복사해서 써보세요!**\n> \"너는 다정한 동화 작가야. '잠 안 오는 강아지'를 주인공으로 짧은 동화를 써줘. 5세 아이가 이해하기 쉬운 단어만 써야 해!\"",
        "video": "https://www.youtube.com/watch?v=0pL07P0U7P0",
        "link": "https://chatgpt.com"
    },
    "🎨 그림 그리는 꼬마 (Midjourney)": {
        "intro": "상상 속의 풍경을 마법처럼 그려내는 친구예요!",
        "strategy": [
            "**Step 1. 스타일 키워드 추가**: 사진 같은 느낌을 원하면 '--v 6.0'이나 'photorealistic'을 꼭 붙여요.",
            "**Step 2. 조명 조절하기**: 'Golden hour'나 'Soft lighting' 키워드로 분위기를 확 바꿀 수 있어요.",
            "**Step 3. 화면 비율 정하기**: 인스타용은 '--ar 1:1', 영화 같은 느낌은 '--ar 16:9'를 뒤에 써주세요!"
        ],
        "prompt_example": "📍 **복사해서 써보세요!**\n> \"/imagine prompt: A cute white cat wearing a yellow raincoat in the rain, 3d render, claymation style, high detail --ar 1:1\"",
        "video": "https://www.youtube.com/watch?v=9oN_X7l0_4U",
        "link": "https://midjourney.com"
    },
    "📊 발표 왕자님 (Gamma)": {
        "intro": "클릭 몇 번에 반짝반짝한 PPT를 완성해줘요!",
        "strategy": [
            "**Step 1. 뼈대(Outline) 맡기**: 주제 키워드만 던지고 감마가 짜주는 목차를 먼저 확인하세요.",
            "**Step 2. AI 편집기 활용**: 특정 슬라이드만 마음에 안 들면 '이 페이지를 좀 더 전문적인 차트로 바꿔줘'라고 채팅으로 말하세요.",
            "**Step 3. 폰트/테마 일괄 변경**: 한 번의 클릭으로 전체 분위기를 브랜드 컬러에 맞게 변신시킬 수 있어요!"
        ],
        "prompt_example": "📍 **주제 입력 팁!**\n> \"친환경 에너지의 중요성에 대한 초등학생용 발표 자료를 만들어줘. 사진은 자연 위주로 넣어줘.\"",
        "video": "https://www.youtube.com/watch?v=uK8f_A6KIdM",
        "link": "https://gamma.app"
    }
}

# 5. 화면 레이아웃 구성
selected_tool = st.sidebar.selectbox("🎀 어떤 요정을 만날까요?", list(recipes.keys()))
data = recipes[selected_tool]

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown(f"### {selected_tool}")
    st.write(f"*{data['intro']}*")
    
    st.markdown('<div class="strategy-card">', unsafe_allow_html=True)
    st.markdown("#### 👩‍🍳 시크릿 사용 레시피")
    for step in data['strategy']:
        st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.info(data['prompt_example'])
    st.link_button(f"{selected_tool.split()[-1]} 요정 만나러 가기 ✈️", data['link'])

with col2:
    st.markdown("#### 📺 1분 만에 마스터하는 영상 가이드")
    st.video(data['video'])
    st.caption("출처: 관련 도구 공식 유튜브 채널 및 전문가 튜토리얼")

# 6. 푸터
st.write("---")
st.center_text = st.markdown("<p style='text-align: center;'>오늘도 AI랑 친해지는 달콤한 하루 되세요! 🍭</p>", unsafe_allow_html=True)
