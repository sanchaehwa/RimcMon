import streamlit as st

# 초기 페이지 설정
if "page" not in st.session_state:
    st.session_state.page = "input"

# 초기 데이터 설정
if "name" not in st.session_state:
    st.session_state.name = ""
if "self_intro" not in st.session_state:
    st.session_state.self_intro = ""
if "selected_skills" not in st.session_state:
    st.session_state.selected_skills = []

# 기술 이미지 URL 정의 (전역 변수로 설정)
skills = {
    "Java": "https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white",
    "C": "https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white",
    "Python": "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white",
    "Spring": "https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white",
    "Adobe Illustrator": "https://img.shields.io/badge/adobeillustrator-FF9A00?style=flat-square&logo=adobeillustrator&logoColor=black",
}
##E34F26
# 입력 페이지
if st.session_state.page == "input":
    st.title("내 정보 등록")

    # 이름 입력 필드
    st.session_state.name = st.text_input(
        "이름", value=st.session_state.name, placeholder="이름을 입력하세요"
    )

    # 자기소개 입력 필드
    self_intro_input = st.text_area(
        "자기소개", value=st.session_state.self_intro, placeholder="자기소개를 입력하세요"
    )
    if st.button("자기소개 저장"):
        st.session_state.self_intro = self_intro_input  # 자기소개를 저장
        st.success("자기소개가 저장되었습니다!")

    # 기술 선택
    st.markdown("#### 사용 가능한 기술")
    selected_skills = []
    for skill in skills.keys():
        if st.checkbox(skill, key=skill, value=(skill in st.session_state.selected_skills)):
            selected_skills.append(skill)

    if st.button("스택 추가"):
        st.session_state.selected_skills = selected_skills
        st.success("기술 스택이 저장되었습니다!")

    # "프로필 저장" 버튼
    if st.button("저장하기"):
        st.session_state.page = "display"

# 출력 페이지
elif st.session_state.page == "display":
    st.title("내 정보")

    # 이름을 수정 불가능한 텍스트 박스에 표시
    st.text_input("이름", value=st.session_state.name, disabled=True)

    # 자기소개를 수정 불가능한 텍스트 박스에 표시
    st.text_area("자기소개", value=st.session_state.self_intro, disabled=True)

    # 기술 출력
    if st.session_state.selected_skills:
        st.write("**사용 가능한 기술:**")
        for skill in st.session_state.selected_skills:
            st.image(skills[skill], width=50)

    # "수정 페이지로 이동" 버튼
    if st.button("내 정보 수정"):
        st.session_state.page = "input"