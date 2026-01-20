import streamlit as st
import time
import pandas as pd

# 1. 페이지 설정
st.set_page_config(
    page_title="MBTI 성향 분석기",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 화려한 디자인을 위한 스타일 커스텀
st.markdown("""
    <style>
    /* 메인 배경색 및 글꼴 */
    .stApp {
        background-color: #FDFEFF;
    }
    /* 카드 스타일 */
    .result-card {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #E1E4E8;
    }
    /* 강조 텍스트 */
    .highlight {
        color: #6C63FF;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 사이드바 (사용자 입력)
with st.sidebar:
    st.title("🧩 Profile")
    name = st.text_input("당신의 이름은?", placeholder="홍길동")
    st.write("---")
    st.caption("질문에 솔직하게 답할수록 정확한 데이터가 산출됩니다.")
    
    # 테마 선택 (UI용)
    theme_color = st.color_picker("분석 리포트 포인트 컬러 선택", "#6C63FF")

# 4. 메인 화면 레이아웃
st.title("✨ AI MBTI Insight Dashboard")
st.markdown(f"**{name if name else '사용자'}**님, 당신의 내면을 데이터로 시각화합니다.")
st.divider()

col1, col2 = st.columns([1, 1.2], gap="large")

# --- 왼쪽: 질문 섹션 ---
with col1:
    st.subheader("📝 Self-Assessment")
    
    with st.expander("1. 에너지의 방향", expanded=True):
        q1 = st.select_slider(
            "혼자 있을 때 에너지가 충전되나요, 사람들과 있을 때 충전되나요?",
            options=["혼자가 좋아(I)", "중간", "사람이 좋아(E)"]
        )
    
    with st.expander("2. 정보 인식 및 판단", expanded=True):
        q2 = st.radio("문제를 해결할 때 더 중요하게 생각하는 것은?", 
                      ["객관적 사실과 논리(T)", "주변 사람의 상황과 감정(F)"])
        
    with st.expander("3. 생활 양식", expanded=True):
        q3 = st.checkbox("나는 계획이 틀어지면 스트레스를 받는다 (J/P)")

    if st.button("데이터 분석 시작 →"):
        with st.status("알고리즘 연산 중...", expanded=True) as status:
            st.write("응답 패턴 분석 중...")
            time.sleep(1)
            st.write("유사 그룹 데이터 매칭 중...")
            time.sleep(1)
            status.update(label="분석 완료!", state="complete", expanded=False)
        st.session_state['done'] = True
        st.balloons()

# --- 오른쪽: 결과 섹션 ---
with col2:
    if 'done' in st.session_state:
        st.subheader("📊 Analysis Result")
        
        # 결과 카드 디자인
        st.markdown(f"""
        <div class="result-card">
            <h3>분석 결과: <span class="highlight">ENFJ (사회운동가형)</span></h3>
            <p>당신은 타인의 성장을 돕고 공동체의 화합을 중요시하는 리더십을 가지고 있습니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # 간격
        
        # Streamlit 내장 차트를 이용한 시각화 (추가 라이브러리 불필요)
        st.write("📍 **성향 지표(Metrics)**")
        
        m_col1, m_col2 = st.columns(2)
        m_col1.metric("외향성(E)", "82%", "12%")
        m_col2.metric("논리성(T)", "45%", "-5%")
        
        # 가상의 데이터 차트
        chart_data = pd.DataFrame({
            "지표": ["에너지", "직관", "논리", "계획"],
            "수치": [80, 65, 45, 90]
        })
        st.bar_chart(data=chart_data, x="지표", y="수치", color=theme_color)
        
        st.success("💡 **Tip:** 당신은 오늘 협업을 할 때 가장 큰 성과를 낼 수 있습니다.")
        
    else:
        st.info("왼쪽 문항을 완료하고 '분석 시작' 버튼을 클릭하면 결과 대시보드가 활성화됩니다.")
        # 가상의 빈 차트 모양만 보여주기
        st.image("https://via.placeholder.com/600x400.
