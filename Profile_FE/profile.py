import streamlit as st
import json
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from Python_Script_Profile.insert_to_db import send_data_to_server, combine_data_for_db

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# 초기 상태 설정
def initialize_state():
    if "page" not in st.session_state:
        st.session_state.page = "input"
    if "name" not in st.session_state:
        st.session_state.name = ""
    if "self_intro" not in st.session_state:
        st.session_state.self_intro = ""
    if "selected_skills" not in st.session_state:
        st.session_state.selected_skills = []

# skill 이미지 URL 정의
def get_skills():
    return {
        "Java": "https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white",
        "C": "https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white",
        "Python": "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white",
        "Spring": "https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white",
        "Adobe Illustrator": "https://img.shields.io/badge/adobeillustrator-FF9A00?style=flat-square&logo=adobeillustrator&logoColor=black",
    }

# 상태 저장 함수
def save_changes():
    st.session_state.page = "display"
    json_data = json.dumps(combine_data_for_db(get_skills(), st.session_state), ensure_ascii=False, indent=4)
    logging.info("저장된 정보: %s", json_data)
    st.success("정보가 저장되었습니다.")

# 입력 페이지 렌더링
def render_input_page(skills):
    st.title("내 정보 등록")

    # 이름 입력
    name = st.text_input(
        "이름",
        value=st.session_state.name,
        placeholder="이름을 입력하세요",
    )
    
    # 자기소개 입력
    self_intro = st.text_area(
        "자기소개",
        value=st.session_state.self_intro,
        placeholder="자기소개를 입력하세요",
    )

    # skill 선택
    st.markdown("#### 사용 가능한 기술")
    selected_skills = []
    for skill in skills.keys():
        if st.checkbox(skill, key=skill, value=(skill in st.session_state.selected_skills)):
            selected_skills.append(skill)

    # 저장 버튼
    if st.button("저장하기"):
        st.session_state.name = name
        st.session_state.self_intro = self_intro
        st.session_state.selected_skills = selected_skills
        save_changes()

# 출력 페이지 렌더링
def render_display_page(skills):
    st.title("내 정보")

    # 이름과 자기소개 표시
    st.text_input("이름", value=st.session_state.name, disabled=True)
    st.text_area("자기소개", value=st.session_state.self_intro, disabled=True)

    # skill 출력
    if st.session_state.selected_skills:
        st.write("**사용 가능한 기술:**")
        for skill in st.session_state.selected_skills:
            st.image(skills[skill], width=50)

    # 수정 버튼
    if st.button("내 정보 수정"):
        st.session_state.page = "input"

# 메인 함수
def main():
    initialize_state()
    skills = get_skills()
    if st.session_state.page == "input":
        render_input_page(skills)
    elif st.session_state.page == "display":
        render_display_page(skills)
        # 데이터가 저장되면 서버로 전송
        send_data_to_server(combine_data_for_db(skills, st.session_state))

# Streamlit 실행
if __name__ == "__main__":
    main()