import streamlit as st
import json
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
#rom Python_Script_Profile.insert_to_db import send_data_to_server, combine_data_for_db 

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
def initialize_state():
    #페이지 설정
    if "page" not in st.session_state:
        st.session_state.page = "input"
    
    if "name" not in st.session_state:
        st.session_state.name = "양화영"
        #st.session_state.name = get_user_name_from_db()  #DB에서 이름 가져오기

    if "password" not in st.session_state:
        st.session_state.password = "1234"  # 초기 비밀번호 설정
    #st.session_state.password = get_user_password_from_db()
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
    st.session_state.self_intro = st.session_state.self_intro
    #json_data = json.dumps(combine_data_for_db(get_skills(), st.session_state), ensure_ascii=False, indent=4)
   # logging.info("저장된 정보: %s", json_data)
    #send_data_to_server(combine_data_for_db(get_skills(), st.session_state))  # 서버로 데이터 전송
    st.success("정보가 저장되었습니다.")

# 입력 페이지
def render_input_page(skills):
    st.title("내 정보 등록")
    st.text_input("이름", value=st.session_state.name, disabled=True)
    st.text_input("비밀번호", value=st.session_state.password, type="password", disabled=True)

    # 자기소개 입력 필드
    self_intro_input = st.text_area(
        "자기소개", value=st.session_state.self_intro, placeholder="자기소개를 입력하세요"
    )
    st.session_state.self_intro = self_intro_input

    # 스택 선택
    st.markdown("#### 사용 가능한 기술")
    st.session_state.selected_skills = [
        skill for skill in skills.keys() if st.checkbox(skill, key=skill, value=(skill in st.session_state.selected_skills))
    ]

    if st.button("저장하기"):
        if not st.session_state.self_intro.strip():  # 자기소개가 공백 또는 비어 있는 경우
            st.warning("자기소개를 입력해주세요!")
        else:
            save_changes()

# 출력 페이지
def render_display_page(skills):
    st.title("내 정보")
    st.text_input("이름", value=st.session_state.name, disabled=True)
    st.text_input("비밀번호", value=st.session_state.password, type="password", disabled=True)
    st.text_area("자기소개", value=st.session_state.self_intro, disabled=True)

    # 기술 출력
    if st.session_state.selected_skills:
        st.write("**사용 가능한 기술:**")
        for skill in st.session_state.selected_skills:
            st.image(skills[skill], width=50)

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
       # send_data_to_server(combine_data_for_db(skills, st.session_state))

# Streamlit 실행
if __name__ == "__main__":
    main()