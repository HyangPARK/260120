import json
from datetime import date

import streamlit as st
from PIL import Image


# -----------------------------
# Page Config (아이콘 이미지로 변경)
# -----------------------------
def load_icon(path: str):
    """아이콘 파일이 없을 때를 대비한 안전 로더."""
    try:
        return Image.open(path)
    except Exception:
        return None


app_icon = load_icon("assets/app_icon.png")

st.set_page_config(
    page_title="자기소개서 웹앱",
    page_icon=app_icon if app_icon else "📝",  # 이미지 없으면 대체 이모지
    layout="wide",
)

# -----------------------------
# Header
# -----------------------------
top_left, top_right = st.columns([1, 5], gap="medium")
with top_left:
    if app_icon:
        st.image(app_icon, width=72)  # 앱 로고(상단 표시)
    else:
        st.markdown("### 📝")
with top_right:
    st.title("자기소개서 웹앱")

