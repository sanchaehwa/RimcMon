import streamlit as st
import json
import os

# JSON 파일 경로
JSON_FILE = "user_data.json"

# JSON 파일 읽기
def read_json():
    if not os.path.exists(JSON_FILE):
        return {"users": []}  # 파일이 없으면 기본 구조 반환
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# JSON 파일 쓰기
def write_json(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 초기화 함수
def initialize_state(user_data):
    if "self_intro" not in st.session_state:
        data = read_json()
        user_profile = next((user["profile"] for user in data["users"] if user["name"] == user_data["name"]), {})
        st.session_state.self_intro = user_profile.get("self_intro", "")
    if "selected_skills" not in st.session_state:
        st.session_state.selected_skills = user_profile.get("skills", [])
    if "user_data" not in st.session_state:
        st.session_state.user_data = user_data
    if "page" not in st.session_state:
        st.session_state.page = "display"

# 기술 스택 이미지 URL 정의
def get_skills():
    return {
        "Java": "https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white",
        "C": "https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white",
        "Python": "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white",
        "Spring": "https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white",
        "Adobe Illustrator": "https://img.shields.io/badge/adobeillustrator-FF9A00?style=flat-square&logo=adobeillustrator&logoColor=black",
    }

# 로그아웃 함수
def logout():
    st.session_state.clear()
    st.session_state.current_page = "login"

# 데이터 저장 함수
def save_user_data(user_data):
    data = read_json()  # 기존 데이터 불러오기
    # 사용자 이름에 해당하는 기존 데이터를 찾아 수정
    for user in data["users"]:
        if user["name"] == user_data["name"]:
            user["profile"] = {
                "self_intro": st.session_state.self_intro,
                "skills": st.session_state.selected_skills,
            }
            break
    else:
        # 신규 사용자일 경우 추가
        data["users"].append({
            "name": user_data["name"],
            "password": user_data["password"],
            "profile": {
                "self_intro": st.session_state.self_intro,
                "skills": st.session_state.selected_skills,
            }
        })
    write_json(data)  # 업데이트된 데이터를 JSON 파일에 저장

# 입력 페이지 렌더링
def render_input_page(skills):
    st.sidebar.button("로그아웃", on_click=logout)
    st.title("내 정보 등록")
    user_data = st.session_state.user_data
    st.text_input("이름", value=user_data.get("name", ""), disabled=True)
    st.text_input("비밀번호", value=user_data.get("password", ""), type="password", disabled=True)

    # 자기소개 입력
    self_intro_input = st.text_area("자기소개", value=st.session_state.self_intro, placeholder="자기소개를 입력하세요")
    st.session_state.self_intro = self_intro_input

    # 기술 선택
    st.markdown("#### 사용 가능한 기술")
    st.session_state.selected_skills = [
        skill for skill in skills.keys() if st.checkbox(skill, key=skill, value=(skill in st.session_state.selected_skills))
    ]

    if st.button("저장하기"):
        if not st.session_state.self_intro.strip():
            st.warning("자기소개를 입력해주세요!")
        else:
            save_user_data(st.session_state.user_data)
            st.session_state.page = "display"
            st.success("정보가 저장되었습니다.")

# 출력 페이지 렌더링
def render_display_page(skills):
    st.sidebar.button("로그아웃", on_click=logout)
    st.title("내 정보")
    user_data = st.session_state.user_data

    st.text_input("이름", value=user_data.get("name", ""), disabled=True)
    st.text_input("비밀번호", value=user_data.get("password", ""), type="password", disabled=True)
    st.text_area("자기소개", value=st.session_state.self_intro, disabled=True)

    # 선택한 기술 출력
    if st.session_state.selected_skills:
        st.markdown("#### 사용 가능한 기술")
        for skill in st.session_state.selected_skills:
            st.image(skills.get(skill, ""), width=50)

    if st.button("내 정보 수정"):
        st.session_state.page = "input"

# 메인 함수
def main(user_data):
    initialize_state(user_data)
    skills = get_skills()

    if st.session_state.page == "input":
        render_input_page(skills)
    elif st.session_state.page == "display":
        render_display_page(skills)
