import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="AI Strategy Hub", page_icon="🤖", layout="wide")

# 2. 간단한 데이터베이스 (가상 데이터)
# 실제 앱을 만들 때는 이 부분을 JSON이나 CSV 파일로 관리하면 더 좋습니다.
ai_tools = {
    "글쓰기 및 분석": [
        {
            "name": "ChatGPT",
            "strategy": "복잡한 추론과 데이터 분석에 활용하세요. 특히 o1/o3 모델은 문제 해결에 강력합니다.",
            "video_url": "https://www.youtube.com/watch?v=0pL07P0U7P0", # 예시 URL
            "resource": "https://openai.com/chatgpt"
        },
        {
            "name": "Claude",
            "strategy": "긴 문맥의 문서 분석이나 코딩 가이드가 필요할 때 Artifacts 기능을 활용해 보세요.",
            "video_url": "https://www.youtube.com/watch?v=fS_n_Y_5hG0",
            "resource": "https://claude.ai"
        }
    ],
    "이미지 및 비디오": [
        {
            "name": "Midjourney",
            "strategy": "예술적이고 감각적인 결과물이 필요할 때 상세 프롬프트 조합법을 익혀 사용하세요.",
            "video_url": "https://www.youtube.com/watch?v=9oN_X7l0_4U",
            "resource": "https://www.midjourney.com"
        }
    ],
    "검색 및 리서치": [
        {
            "name": "Perplexity",
            "strategy": "실시간 뉴스나 학술 자료를 찾을 때 출처 인용 기능을 통해 팩트 체크를 병행하세요.",
            "video_url": "https://www.youtube.com/watch?v=7XGidM2_M04",
            "resource": "https://www.perplexity.ai"
        }
    ]
}

# 3. 메인 화면 UI
st.title("🤖 AI Strategy Hub")
st.markdown("#### 2026년형 AI 도구 활용 전략 가이드")
st.info("카테고리를 선택하고 각 도구의 최적 사용 전략을 확인하세요.")

# 카테고리 선택
category = st.selectbox("🎯 관심 있는 분야를 선택하세요", list(ai_tools.keys()))

st.divider()

# 4. 도구별 카드 레이아웃
for tool in ai_tools[category]:
    with st.container():
        col1, col2 = st.columns([1, 1.5], gap="medium")
        
        with col1:
            st.subheader(f"✨ {tool['name']}")
            st.markdown(f"**활용 전략:**\n{tool['strategy']}")
            st.link_button(f"{tool['name']} 바로가기", tool['resource'])
            
        with col2:
            st.markdown("**🎬 가이드 및 활용 사례 영상**")
            # 유튜브 동영상 임베딩
            st.video(tool['video_url'])
            
        st.write("") # 간격 조절
        st.divider()

# 5. 하단 정보
st.caption("© 2026 AI Strategy Hub - 데이터는 최신 트렌드에 따라 지속적으로 업데이트됩니다.")
