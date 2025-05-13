import streamlit as st

# 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["📊 회계사", "📂 행정관", "🔍 데이터 분석가"],
    "ISFJ": ["👩‍🏫 교사", "🏥 간호사", "📝 문서 관리원"],
    "INFJ": ["🎨 예술가", "🌱 심리상담사", "📚 인문학자"],
    "INTJ": ["🧠 연구원", "💼 경영 전략가", "🔧 엔지니어"],
    "ISTP": ["🛠️ 기술자", "🚘 자동차 정비사", "🔍 탐정"],
    "ISFP": ["🎨 디자이너", "🧵 공예가", "📸 사진작가"],
    "INFP": ["📝 작가", "💡 창작자", "🎭 배우"],
    "INTP": ["💻 프로그래머", "🔬 연구자", "🧩 문제 해결 전문가"],
    "ESTP": ["📈 마케팅 전문가", "🚗 자동차 딜러", "🎤 이벤트 기획자"],
    "ESFP": ["🎭 연예인", "🎙️ 아나운서", "👗 스타일리스트"],
    "ENFP": ["🌍 사회운동가", "📖 작가", "🎨 콘텐츠 크리에이터"],
    "ENTP": ["💡 혁신가", "🗣️ 토론가", "🧩 발명가"],
    "ESTJ": ["💼 관리자", "🔧 공장장", "📊 생산 관리자"],
    "ESFJ": ["🏫 교사", "🧑‍⚕️ 간호사", "🎉 이벤트 플래너"],
    "ENFJ": ["💬 상담사", "🌍 국제 협력 전문가", "📢 홍보 전문가"],
    "ENTJ": ["💼 경영자", "⚖️ 변호사", "📊 프로젝트 관리자"],
}

# 웹 페이지 제목과 스타일 설정
st.set_page_config(page_title="MBTI 직업 추천 💼", page_icon="🌟", layout="centered")
st.title("🌟 나에게 맞는 직업 찾기! 🌟")
st.markdown("#### MBTI 유형을 선택하면 추천 직업을 알려드릴게요! 💼✨")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox(
    "당신의 MBTI 유형을 선택하세요! 🌈",
    list(mbti_jobs.keys())
)

# 추천 직업 결과
if selected_mbti:
    st.write(f"### 당신의 MBTI 유형: {selected_mbti} 🌟")
    st.markdown("#### 당신에게 추천하는 직업들! 💼")

    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

# 이모지로 꾸민 하단 텍스트
st.markdown("---")
st.markdown("💖 **여러분의 꿈을 응원합니다!** 💪")
st.markdown("🚀 **다양한 진로를 탐색해보세요!** 🎉")
