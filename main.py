import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="AI Level-Up Shop", page_icon="🍭", layout="wide")

# 2. 더 귀엽고 구체적인 CSS 커스텀
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F2; } /* 따뜻한 아이보리 배경 */
    .level-card {
        padding: 20px;
        border-radius: 25px;
        margin-bottom: 25px;
        color: #444;
    }
    .beginner { background-color: #E3F2FD; border: 3px solid #90CAF9; } /* 하늘색 */
    .intermediate { background-color: #FFF3E0; border: 3px solid #FFCC80; } /* 오렌지 */
    .advanced { background-color: #F3E5F5; border: 3px solid #CE93D8; } /* 보라 */
    
    .strategy-step {
        background: white;
        padding: 10px 15px;
        border-radius: 12px;
        margin: 8px 0;
        font-size: 0.95rem;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.03);
    }
    .emoji-title { font-size: 1.5rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 구성 (난이도별 도구 및 구체적 전략)
ai_data = {
    "🌱 초보 (AI랑 친해져요)": {
        "class": "beginner",
        "tools": [
            {
                "name": "ChatGPT (대화형 비서)",
                "desc": "말만 하면 다 해주는 가장 친절한 친구!",
                "strategy": [
                    "📍 **비유해서 물어보기**: '중학생도 이해할 수 있게 양자역학을 설명해줘'라고 해보세요.",
                    "📍 **예시 요청하기**: 결과가 모호하면 '실제 사례 3가지만 들어줘'라고 구체화하세요.",
                    "📍 **번역&요약**: 긴 영어 기사를 복사해서 '한글로 세 줄 요약해줘'라고 하면 끝!"
                ],
                "video": "https://www.youtube.com/watch?v=0pL07P0U7P0",
                "link": "https://chatgpt.com"
            },
            {
                "name": "Canva Magic Design (디자인)",
                "desc": "제목만 넣으면 포스터가 뚝딱!",
                "strategy": [
                    "📍 **템플릿 활용**: '생일 파티'라고 검색하고 AI가 추천하는 디자인을 고르세요.",
                    "📍 **매직 편집**: 사진에서 지우고 싶은 부분만 쓱쓱 문지르면 감쪽같이 사라져요!"
                ],
                "video": "https://www.youtube.com/watch?v=un95S_4XvXU",
                "link": "https://www.canva.com"
            }
        ]
    },
    "🌿 중급 (실무에 써먹어요)": {
        "class": "intermediate",
        "tools": [
            {
                "name": "Perplexity (AI 검색)",
                "desc": "구글링보다 빠른 근거 기반 리서치 도구!",
                "strategy": [
                    "📍 **출처 확인**: 답변마다 붙은 번호를 클릭해 원문 기사를 직접 확인하는 습관을 들이세요.",
                    "📍 **Focus 기능**: 'Academic' 모드로 설정하면 학술 논문 위주로 검색해줘요.",
                    "📍 **연관 질문 탐색**: 하단에 뜨는 '사람들이 더 궁금해하는 질문'을 클릭해 지식을 확장하세요."
                ],
                "video": "https://www.youtube.com/watch?v=7XGidM2_M04",
                "link": "https://www.perplexity.ai"
            },
            {
                "name": "Gamma (발표자료)",
                "desc": "아이디어 메모가 바로 슬라이드가 되는 마법!",
                "strategy": [
                    "📍 **텍스트로 카드 추가**: 슬라이드 중간에 내용을 더 넣고 싶으면 채팅창에 명령어를 치세요.",
                    "📍 **웹사이트 모드**: 발표 자료를 웹사이트 형태로 배포해 링크만 공유해보세요."
                ],
                "video": "https://www.youtube.com/watch?v=uK8f_A6KIdM",
                "link": "https://gamma.app"
            }
        ]
    },
    "🔥 고수 (나만의 AI 만들기)": {
        "class": "advanced",
        "tools": [
            {
                "name": "Cursor (AI 코딩)",
                "desc": "코딩을 몰라도 앱을 만들 수 있게 해주는 도구!",
                "strategy": [
                    "📍 **Ctrl+K (명령)**: 특정 코드 영역을 잡고 '이 로직을 더 효율적으로 바꿔줘'라고 지시하세요.",
                    "📍 **@ 기호 활용**: '@Files'나 '@Docs'를 써서 특정 파일 내용을 AI에게 참조시키세요.",
                    "📍 **에러 자동 수정**: 터미널에 뜬 에러를 복사해서 'Fix this' 버튼만 누르면 해결책을 줍니다."
                ],
                "video": "https://www.youtube.com/watch?v=zv8Z_6ZzX88",
                "link": "https://www.cursor.com"
            },
            {
                "name": "D-ID (비디오 생성)",
                "desc": "사진 한 장으로 말하는 아바타 영상을 만들어요!",
                "strategy": [
                    "📍 **음성 파일 업로드**: 텍스트 입력 대신 본인 목소리를 녹음해 올리면 훨씬 자연스러워요.",
                    "📍 **표정 제어**: 스크립트 사이사이에 감정(Happy, Serious)을 지정해 생동감을 높이세요."
                ],
                "video": "https://www.youtube.com/watch?v=XzW3vj_N8l0",
                "link": "https://www.d-id.com"
            }
        ]
    }
}

# 4. 메인 UI
st.title("🍭 AI Level-Up Candy Shop")
st.write("당신의 AI 숙련도에 딱 맞는 **'맞춤 사탕 가이드'**를 골라보세요!")
st.divider()

# 숙련도 선택 라디오 버튼
level_choice = st.radio("✨ 당신의 AI 레벨은 어느 정도인가요?", list(ai_data.keys()), horizontal=True)

# 5. 선택된 레벨의 도구 전시
selected_level = ai_data[level_choice]
st.markdown(f'<div class="{selected_level["class"]} level-card">', unsafe_allow_html=True)
st.subheader(f"💎 {level_choice} 추천 도구 리스트")

for tool in selected_level["tools"]:
    with st.expander(f"📌 {tool['name']}", expanded=True):
        col1, col2 = st.columns([1, 1.2])
        
        with col1:
            st.markdown(f"**{tool['desc']}**")
            st.write("---")
            st.markdown("**👩‍🏫 마스터 전략:**")
            for step in tool['strategy']:
                st.markdown(f'<div class="strategy-step">{step}</div>', unsafe_allow_html=True)
            st.link_button("도구 사용해보기 🚀", tool['link'])
            
        with col2:
            st.markdown("**📺 실전 활용 영상**")
            st.video(tool['video'])

st.markdown('</div>', unsafe_allow_html=True)

# 6. 푸터
st.divider()
st.center_text = st.markdown("<p style='text-align: center;'>레벨 업을 응원해요! 궁금한 건 언제든 물어보세요 🧁</p>", unsafe_allow_html=True)
