import streamlit as st
import json
import os
from profile import main as profile_main  # 이미 구현된 프로필 페이지를 import

# JSON 파일 경로 설정
DATA_FILE = "user_data.json"

# 초기화 함수
def initialize_session():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    if "user_data" not in st.session_state:
        st.session_state.user_data = None  # 현재 로그인된 사용자 정보 저장

# 데이터 파일 로드
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"users": []}  # 파일이 없으면 빈 데이터 반환

# 데이터 파일 저장
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 사용자 조회 함수
def get_user_from_db(username, password):
    data = load_data()
    for user in data["users"]:
        if user["name"] == username and user["password"] == password:
            return user
    return None

# 사용자 등록 함수
def insert_user_to_db(username, password):
    data = load_data()
    new_user = {"name": username, "password": password, "profile": {"self_intro": "", "skills": []}}
    data["users"].append(new_user)
    save_data(data)  # 변경된 데이터를 저장
    return new_user

# 로그인 페이지
def login_page():
    st.title("로그인")
    username = st.text_input("이름", placeholder="사용자 이름을 입력하세요")
    password = st.text_input("비밀번호", placeholder="비밀번호를 입력하세요", type="password")

    if st.button("로그인"):
        user_data = get_user_from_db(username, password)  # 사용자 조회
        if user_data:
            st.success(f"환영합니다, {username}님!")
            st.session_state.user_data = user_data  # 로그인된 사용자 정보 저장
            st.session_state.current_page = "profile"  # 프로필 페이지로 이동
        else:
            st.error("로그인 실패! 이름 또는 비밀번호를 확인하세요.")

    if st.button("신규 사용자 등록"):
        st.session_state.current_page = "register"

# 신규 사용자 등록 페이지
def register_page():
    st.title("신규 사용자 등록")
    username = st.text_input("이름", placeholder="사용자 이름을 입력하세요")
    password = st.text_input("비밀번호", placeholder="비밀번호를 입력하세요", type="password")

    if st.button("등록하기"):
        if len(password) < 4:  # 4자리 이상이어야만 가능하게
            st.error("비밀번호는 최소 4자리 이상으로 설정해주세요")
        elif not username.strip():
            st.error("이름을 입력해주세요")
        elif any(user["name"] == username for user in load_data()["users"]):
            st.error("이미 존재하는 사용자 이름입니다. 다른 이름을 사용해주세요!")
        else:
            # 사용자 정보 등록
            new_user = insert_user_to_db(username, password)
            st.success(f"사용자 '{username}' 등록이 완료되었습니다!")
            
            # 등록 후 로그인
            st.session_state.user_data = new_user
            st.session_state.current_page = "profile"  # 프로필 페이지로 이동

# 메인 함수
def main():
    initialize_session()
    # 네비게이션 로직
    if st.session_state.current_page == "login":
        login_page()
    elif st.session_state.current_page == "profile":
        profile_main(st.session_state.user_data)  # 사용자 데이터를 프로필 페이지로 전달
    elif st.session_state.current_page == "register":
        register_page()

# 실행
if __name__ == "__main__":
    main()
