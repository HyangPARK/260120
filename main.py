import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="데이터 분석 앱", layout="wide")

st.title("📊 데이터 분석 및 결과 리포트")
st.write("데이터를 업로드하면 자동으로 분석 결과를 생성합니다.")

# --- 1. 데이터 수집 ---
uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # --- 2. 데이터 분석 ---
    st.subheader("✅ 데이터 미리보기")
    st.write(df.head())
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📊 **데이터 요약 통계**")
        st.write(df.describe())

    # --- 3. 시각화 ---
    with col2:
        st.write("📈 **변수 간 상관관계 시각화**")
        # 숫자형 컬럼만 선택
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if len(numeric_cols) >= 2:
            x_axis = st.selectbox("X축 선택", numeric_cols)
            y_axis = st.selectbox("Y축 선택", numeric_cols)
            
            fig = px.scatter(df, x=x_axis, y=y_axis, trendline="ols")
            st.plotly_chart(fig, use_container_width=True)
else:
    st.info("왼쪽 사이드바에서 파일을 업로드해 주세요.")
