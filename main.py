import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Ultimate AI Strategy Guide", page_icon="💡", layout="wide")

# 2. 확장된 AI 도구 데이터베이스
ai_database = {
    "💻 코딩 & 개발": [
        {
            "name": "GitHub Copilot",
            "strategy": "단순 반복 코드는 주석으로 지시하고, 전체 프로젝트의 맥락을 이해시켜 리팩토링에 활용하세요.",
            "video_url": "https://www.youtube.com/watch?v=Fi3AJZZregQ",
            "resource": "https://github.com/features/copilot"
        },
        {
            "name": "Cursor",
            "strategy": "코드베이스 전체를 인덱싱하여 복잡한 버그 수정이나 라이브러리 마이그레이션에 사용하세요.",
            "video_url": "https://www.youtube.com/watch?v=zv8Z_6ZzX88",
            "resource": "https://www.cursor.com/"
        }
    ],
    "🎨 이미지 & 디자인": [
        {
            "name": "Canva Magic Studio",
            "strategy": "디자인 초보자라면 텍스트를 입력해 바로 템플릿을 생성하고, 배경 제거 및 매직 리사이즈 기능을 적극 활용하세요.",
            "video_url": "https://www.youtube.com/watch?v=un95S_4XvXU",
            "resource": "https://www.canva.com/magic-home/"
        },
        {
            "name": "Leonardo.ai",
            "strategy": "특정 화풍을 학습시킨 LoRA 모델을 선택하여 브랜드만의 일관된 캐릭터나 아이콘을 만드세요.",
            "video_url": "https://www.youtube.com/watch?v=FjS6o9UfKzM",
            "resource": "https://leonardo.ai/"
        }
    ],
    "📈 마케팅 & 생산성": [
        {
            "name": "Gamma APP",
            "strategy": "아이디어 메모만으로 발표 슬라이드를 만드세요. AI 편집기 기능을 사용해 전체 디자인 톤을 한 번에 변경할 수 있습니다.",
            "video_url": "https://www.youtube.com/watch?v=uK8f_A6KIdM",
            "resource": "https://gamma.app/"
        },
        {
            "name": "Notion AI",
            "strategy": "회의록 요약, 데이터베이스 속성 자동 채우기 기능을 통해 협업 효율을 극대화하세요.",
            "video_url": "https://www.youtube.com/watch?v=vV_XpYf-2mI",
            "resource": "https://www.notion.so/product/ai"
        }
    ]
}

# 3. UI 구현
st.title("💡 AI Tool & Strategy Dashboard")
st.markdown("분야별 최고의 AI 도구와 그에 맞는 **실전 활용 전략**을 확인하세요.")

# 탭 메뉴 구성
tabs = st.tabs(list(ai_database.keys()))

for i, category in enumerate(ai_database.keys()):
    with tabs[i]:
        st.header(f"{category} 솔루션")
        
        for tool in ai_database[category]:
            # 카드 섹션 스타일링
            with st.expander(f"🔍 {tool['name']} 상세 전략 보기", expanded=True):
                col1, col2 = st.columns([1, 1], gap="large")
                
                with col1:
                    st.write(f"### {tool['name']}")
                    st.success(f"**📌 핵심 전략:**\n\n{tool['strategy']}")
                    st.link_button("공식 홈페이지 방문", tool['resource'])
                
                with col2:
                    st.info("📺 **참고 영상 가이드**")
                    # 유튜브 영상 연결
                    st.video(tool['video_url'])

# 4. 하단 추가 자료 섹션
st.divider()
st.subheader("🔗 유용한 리서치 자료")
col_res1, col_res2, col_res3 = st.columns(3)
col_res1.markdown("[State of AI 2024 Report](https://www.stateof.ai/)")
col_res2.markdown("[AI Tool Directory (There's an AI for that)](https://theresanaiforthat.com/)")
col_res3.markdown("[Prompt Engineering Guide](https://www.promptingguide.ai/kr)")
