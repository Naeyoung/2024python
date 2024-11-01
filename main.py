

import streamlit as st

# 타이틀과 설명 추가
st.title('🔮 나의 첫 스트림릿 웹앱 - MBTI 분석 🔮')
st.write("안녕하세요! MBTI 유형을 선택하고 본인의 특성을 확인해보세요! 📊")

# 사용자 입력 섹션
name = st.text_input('이름을 입력해주세요 : ')
mbti = st.selectbox('MBTI를 선택해주세요', [
    'ENTJ', 'INTJ', 'ENTP', 'INTP', 'ENFJ', 'INFJ', 'ENFP', 'INFP',
    'ESTJ', 'ISTJ', 'ESFJ', 'ISFJ', 'ESTP', 'ISTP', 'ESFP', 'ISFP'
])

# MBTI 설명 데이터
mbti_descriptions = {
    'ENTJ': "💼 **ENTJ** - 리더십과 전략적 사고의 대명사! ENTJ는 목표 지향적이며 문제 해결에 탁월한 능력을 가지고 있습니다. 다른 사람들을 이끄는 것을 즐기며, 미래의 비전을 설정하고 실현하는 데 적극적입니다. 📈",
    'INTJ': "🧠 **INTJ** - 논리적이고 창의적인 전략가! INTJ는 자신만의 비전과 목표를 설정하며 이를 달성하기 위해 계획을 세웁니다. 깊이 있는 통찰력을 통해 복잡한 문제를 해결하는 데 능합니다. 🔍",
    'ENTP': "💡 **ENTP** - 혁신적이고 논쟁을 즐기는 발명가! ENTP는 끊임없이 새로운 아이디어를 탐구하고 토론을 즐깁니다. 변화와 도전을 환영하며, 문제에 대한 다양한 관점을 탐구하는 성향이 있습니다. 🚀",
    'INTP': "🧩 **INTP** - 분석적이고 호기심 많은 사색가! INTP는 지식과 진리를 탐구하며, 복잡한 개념을 분석하는 데 뛰어납니다. 논리와 창의력을 결합하여 혁신적인 해결책을 만들어내는 것을 즐깁니다. 🧐",
    'ENFJ': "💖 **ENFJ** - 타인을 돕고 지도하는 따뜻한 리더! ENFJ는 사람들의 성장을 도모하며, 타인에게 긍정적인 변화를 가져다 주는 데 기쁨을 느낍니다. 인간관계를 중요시하며, 주변 사람들에게 영감을 줍니다. 🌟",
    'INFJ': "🌌 **INFJ** - 통찰력과 이상을 가진 이상주의자! INFJ는 깊이 있는 공감 능력과 직관력을 통해 타인의 마음을 이해하고 돕는 데 헌신적입니다. 세상을 더 나은 곳으로 만들고자 하는 비전을 가지고 있습니다. 🌱",
    'ENFP': "🌈 **ENFP** - 자유로운 영혼의 열정가! ENFP는 새로운 가능성을 찾고 다양한 사람들과의 관계를 형성하는 데 흥미를 느낍니다. 창의적이고 활기찬 에너지를 주변에 전파합니다. 🎉",
    'INFP': "🌻 **INFP** - 이상적이며 창의적인 중재자! INFP는 개인적인 가치와 의미를 중요시하며, 자신만의 세계에서 진실과 아름다움을 찾습니다. 인간 내면에 대한 깊은 이해력을 가지고 있습니다. 🎨",
    'ESTJ': "⚖️ **ESTJ** - 현실적이고 체계적인 관리자! ESTJ는 책임감이 강하며, 목표 달성을 위해 체계적으로 계획을 수립합니다. 규율과 효율성을 중요시하며, 상황을 주도적으로 이끌어갑니다. 📋",
    'ISTJ': "📚 **ISTJ** - 성실하고 신뢰할 수 있는 분석가! ISTJ는 원칙을 중시하고, 세세한 부분까지 철저하게 관리합니다. 실용적이고 신중한 성향을 통해 높은 신뢰를 받습니다. 🔍",
    'ESFJ': "🤝 **ESFJ** - 따뜻하고 친절한 사회적 원동력! ESFJ는 주변 사람들과의 관계를 중시하며, 타인을 돕는 것에 기쁨을 느낍니다. 사회적 분위기를 조성하고 사람들을 연결하는 데 능숙합니다. 🎈",
    'ISFJ': "🌷 **ISFJ** - 배려심 깊고 충실한 보호자! ISFJ는 타인의 필요를 민감하게 파악하고, 신뢰를 주는 성격으로 주변 사람들에게 헌신적입니다. 조용하지만 깊은 애정을 표현합니다. 💌",
    'ESTP': "🎯 **ESTP** - 열정적이고 도전적인 활동가! ESTP는 상황에 빠르게 적응하고 실용적인 해결책을 찾습니다. 순간을 즐기며, 모험과 새로운 경험을 추구합니다. 🏆",
    'ISTP': "🔧 **ISTP** - 실용적이고 호기심 많은 장인! ISTP는 문제 해결 능력이 뛰어나며, 새로운 기술을 배우고 적용하는 데 능숙합니다. 탐구와 실험을 통해 최적의 결과를 찾습니다. 🛠️",
    'ESFP': "🎤 **ESFP** - 활기차고 즐거운 연예인! ESFP는 사람들과 어울리며 현재의 순간을 즐깁니다. 주변 사람들을 기쁘게 하고 긍정적인 에너지를 전파하는 데 뛰어납니다. 🎉",
    'ISFP': "🎨 **ISFP** - 감성적이며 예술적인 모험가! ISFP는 감각적이고 섬세한 아름다움을 찾는 데 열정을 가지고 있으며, 자신의 가치관을 표현하는 데 자유롭습니다. 🌺"
}

# 확인 버튼 기능
if st.button('확인!') and name and mbti:
    st.success(f"**{name}님**은 정말 {mbti} 같아보이시네요! 🎉")
    st.write(mbti_descriptions[mbti])  # 선택한 MBTI 유형에 대한 설명 표시

    # 예시: 추가적으로 확률 표시 바 추가
    st.progress(80)  # 예시로 80% 정도 신뢰도
    st.balloons()  # 결과 발표 후 풍선 효과 추가!
else:
    st.warning("이름과 MBTI를 선택 후 확인을 눌러주세요! 😉")
