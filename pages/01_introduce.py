import streamlit as st
from datetime import date
import json

st.set_page_config(
    page_title="자기소개 앱 (Streamlit)",
    page_icon="👤",
    layout="wide",
)

st.title("👤 자기소개 앱")
st.caption("Streamlit에서 실행되는 간단한 자기소개/포트폴리오 생성기")

# -----------------------------
# Sidebar: 기본 설정
# -----------------------------
with st.sidebar:
    st.header("⚙️ 설정")
    theme = st.selectbox("스타일", ["기본", "미니멀", "강조"], index=0)
    show_preview = st.checkbox("미리보기 표시", value=True)
    show_debug = st.checkbox("디버그(입력값 JSON) 표시", value=False)

def badge(text: str):
    return f"<span style='display:inline-block;padding:4px 10px;border-radius:999px;border:1px solid #ddd;margin:2px 6px 2px 0;font-size:0.9rem'>{text}</span>"

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([1.1, 1.2], gap="large")

with left:
    st.subheader("1) 기본 정보 입력")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("이름", value="홍길동")
        role = st.text_input("한 줄 소개(직함/역할)", value="교육공학 연구자 / 원격교육 콘텐츠 기획")
        email = st.text_input("이메일", value="your@email.com")
    with col2:
        phone = st.text_input("연락처(선택)", value="")
        location = st.text_input("지역(선택)", value="Seoul, KR")
        website = st.text_input("웹사이트/포트폴리오 링크(선택)", value="")

    st.markdown("---")

    st.subheader("2) 핵심 소개")
    headline = st.text_input("헤드라인(핵심 문장)", value="학습경험을 설계하고, 데이터를 기반으로 개선합니다.")
    summary = st.text_area(
        "요약(3~6문장 추천)",
        value=(
            "저는 대학 원격수업과 K-MOOC 등 디지털 기반 교육을 설계·운영하며, "
            "학습자 경험(LX)과 학습분석을 연결하는 연구를 수행합니다.\n"
            "생성형 AI를 수업에 통합할 때 신뢰, 투명성, 학습성과를 함께 고려하는 접근을 지향합니다."
        ),
        height=150
    )

    st.markdown("---")

    st.subheader("3) 스킬 & 관심분야")
    skills_raw = st.text_input("스킬(콤마로 구분)", value="교육공학, K-MOOC, 학습분석, 텍스트마이닝, 생성형 AI, 수업설계")
    interests_raw = st.text_input("관심분야(콤마로 구분)", value="HCAI, AI 신뢰/설명가능성, 블렌디드러닝, 원격교육 품질")
    skills = [s.strip() for s in skills_raw.split(",") if s.strip()]
    interests = [s.strip() for s in interests_raw.split(",") if s.strip()]

    st.markdown("---")

    st.subheader("4) 경력/프로젝트 (최대 5개)")
    projects = []
    for i in range(1, 6):
        with st.expander(f"프로젝트 {i} 입력", expanded=(i == 1)):
            p_title = st.text_input(f"프로젝트명 {i}", value=("AI 기반 원격수업 고도화" if i == 1 else ""), key=f"pt{i}")
            p_org = st.text_input(f"기관/팀 {i}", value=("스마트융합교육센터" if i == 1 else ""), key=f"po{i}")
            p_from = st.date_input(f"기간 시작 {i}", value=date(2025, 1, 1) if i == 1 else date.today(), key=f"pf{i}")
            p_to = st.date_input(f"기간 종료 {i}", value=date.today(), key=f"pto{i}")
            p_desc = st.text_area(
                f"설명 {i}",
                value=("실습 중심 온라인 콘텐츠 설계, 학습자 피드백 기반 개선, 운영 데이터 분석" if i == 1 else ""),
                height=90,
                key=f"pd{i}",
            )
            p_stack = st.text_input(f"기술/도구(콤마) {i}", value=("Streamlit, Python, KoNLPy, LMS" if i == 1 else ""), key=f"ps{i}")

        if p_title.strip():
            projects.append({
                "title": p_title.strip(),
                "org": p_org.strip(),
                "from": str(p_from),
                "to": str(p_to),
                "desc": p_desc.strip(),
                "stack": [x.strip() for x in p_stack.split(",") if x.strip()],
            })

    st.markdown("---")

    st.subheader("5) 추가: 링크")
    link_cols = st.columns(3)
    with link_cols[0]:
        linkedin = st.text_input("LinkedIn(선택)", value="")
    with link_cols[1]:
        github = st.text_input("GitHub(선택)", value="")
    with link_cols[2]:
        scholar = st.text_input("Google Scholar(선택)", value="")

# -----------------------------
# Right: Preview
# -----------------------------
profile = {
    "name": name,
    "role": role,
    "headline": headline,
    "summary": summary,
    "email": email,
    "phone": phone,
    "location": location,
    "website": website,
    "skills": skills,
    "interests": interests,
    "projects": projects,
    "links": {
        "linkedin": linkedin,
        "github": github,
        "scholar": scholar,
    }
}

with right:
    st.subheader("미리보기")

    if show_preview:
        # 간단한 테마 스타일
        if theme == "미니멀":
            title_size = "2.0rem"
            accent = "#111"
        elif theme == "강조":
            title_size = "2.3rem"
            accent = "#2E6FCE"
        else:
            title_size = "2.2rem"
            accent = "#333"

        st.markdown(
            f"""
            <div style="padding:18px;border:1px solid #eee;border-radius:16px;">
              <div style="font-size:{title_size};font-weight:800;color:{accent};line-height:1.2;">
                {profile["name"]}
              </div>
              <div style="font-size:1.05rem;color:#666;margin-top:4px;">
                {profile["role"]}
              </div>
              <div style="margin-top:12px;font-size:1.05rem;">
                <b>{profile["headline"]}</b>
              </div>
              <div style="margin-top:10px;color:#444;white-space:pre-wrap;">
                {profile["summary"]}
              </div>

              <hr style="margin:16px 0;border:none;border-top:1px solid #eee;" />

              <div style="display:flex;gap:18px;flex-wrap:wrap;color:#555;">
                <div>📍 {profile["location"] or "-"}</div>
                <div>✉️ {profile["email"] or "-"}</div>
                <div>📞 {profile["phone"] or "-"}</div>
                <div>🔗 {profile["website"] or "-"}</div>
              </div>

              <div style="margin-top:14px;">
                <div style="font-weight:700;margin-bottom:6px;">Skills</div>
                {"".join([badge(s) for s in profile["skills"]]) if profile["skills"] else "<span style='color:#888'>-</span>"}
              </div>

              <div style="margin-top:12px;">
                <div style="font-weight:700;margin-bottom:6px;">Interests</div>
                {"".join([badge(s) for s in profile["interests"]]) if profile["interests"] else "<span style='color:#888'>-</span>"}
              </div>

              <div style="margin-top:14px;">
                <div style="font-weight:700;margin-bottom:6px;">Projects</div>
                {"".join([
                    f"<div style='padding:10px 12px;border:1px solid #eee;border-radius:12px;margin:10px 0;'>"
                    f"<div style='font-weight:750'>{p['title']}</div>"
                    f"<div style='color:#666;margin-top:2px'>{p['org']} · {p['from']} ~ {p['to']}</div>"
                    f"<div style='margin-top:8px;color:#444'>{p['desc']}</div>"
                    f"<div style='margin-top:8px;color:#555'>{''.join([badge(x) for x in p['stack']])}</div>"
                    f"</div>"
                    for p in profile["projects"]
                ]) if profile["projects"] else "<div style='color:#888'>-</div>"}
              </div>

              <div style="margin-top:10px;color:#555;">
                <b>Links:</b>
                {" · ".join([x for x in [profile["links"]["linkedin"], profile["links"]["github"], profile["links"]["scholar"]] if x]) or "-"}
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("내보내기")
    st.download_button(
        label="📥 프로필 JSON 다운로드",
        data=json.dumps(profile, ensure_ascii=False, indent=2).encode("utf-8"),
        file_name="profile.json",
        mime="application/json",
    )

    if show_debug:
        st.code(json.dumps(profile, ensure_ascii=False, indent=2), language="json")

st.markdown("---")
st.caption("Tip: streamlit.io에 올릴 때는 이 파일을 app.py로 저장하고, requirements.txt에 streamlit을 넣으면 됩니다.")

