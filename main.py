import streamlit as st
import time
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="My Inner Compass", page_icon="🧩", layout="wide")

# 화려하고 간결한 디자인을 위한 Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #6C63FF;
        color: white;
        border: none;
    }
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #6C63FF , #3f3d56);
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #6C63FF;
    }
    </style>
    """, unsafe_allow_html=True)

# 헤더 섹션
st.title("🧩 My Inner Compass")
st.markdown("#### 당신의 성향을 분석하고 데이터로 증명합니다.")
st.divider()

# 사이드바: 사용자 입력
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3067/3067451.png", width=100)
    st.header("사용자 정보")
    name = st.text_input("이름", placeholder="홍길동")
    age = st.slider("연령대", 10, 60, 25)
    st.info("모든 답변은 익명으로 처리됩니다.")

# 메인 분석 섹션
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 성향 테스트")
    q1 = st.radio("1. 새로운 사람을 만날 때 나는?", ["에너지를 얻는다 (E)", "혼자 있는게 편하다 (I)"])
    q2 = st.radio("2. 문제를 해결할 때 나는?", ["논리적인 근거가 중요하다 (T)", "사람의 감정이 중요하다 (F)"])
    q3 = st.radio("3. 여행 계획을 세울 때 나는?", ["철저하게 계획한다 (J)", "상황에 맞게 행동한다 (P)"])
    
    if st.button("결과 분석하기"):
        with st.spinner('데이터를 정밀 분석 중입니다...'):
            time.sleep(2)
            st.session_state.analyzed = True
            st.balloons()

# 결과 출력 섹션
if 'analyzed' in st.session_state:
    with col2:
        st.subheader("📊 분석 리포트")
        
        # 가상의 분석 데이터
        mbti_result = "ENFJ" # 예시 결과
        
        # 대시보드 형태의 결과창
        res_col1, res_col2 = st.columns(2)
        res_col1.metric("예상 MBTI", mbti_result)
        res_col2.metric("성향 일치도", "92%", "4%")
        
        # 성향 차트 시각화
        chart_data = pd.DataFrame({
            'Category': ['E/I', 'S/N', 'T/F', 'J/P'],
            'Score': [85, 40, 30, 75]
        })
        fig = px.line_polar(chart_data, r='Score', theta='Category', line_close=True,
                           color_discrete_sequence=['#6C63FF'])
        fig.update_traces(fill='toself')
        fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
        
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("자세한 성향 설명 보기"):
            st.write(f"""
            **{name}**님은 {mbti_result} 유형입니다. 
            당신은 타인의 성장을 돕고 협동하는 것에 큰 가치를 느끼는 리더 타입이군요! 
            데이터에 따르면 당신은 '사회적 관계'에서 가장 큰 효율을 보입니다.
            """)
else:
    with col2:
        st.empty()
        st.info("왼쪽의 질문에 답한 후 '결과 분석하기' 버튼을 눌러주세요.")

# 푸터
st.divider()
st.caption("© 2024 My Inner Compass - Built with Streamlit")
