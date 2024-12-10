import streamlit as st

st.snow()

# 초기 상태 설정
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# 페이지 상태 확인
page = st.session_state["page"]

# 메인 페이지
if page == "main":
    st.image("../img/림크몬.png", use_container_width=True)
    _, exp_col, _ = st.columns([1,5,1])
    with exp_col:
        with st.expander("**📖 림크몬 **"):
            # 림크몬을 누른 후 마크다운 보입니다.
            st.markdown("""
                        안녕하세요 오픈소스SW의 이해 4조입니다🤷🏻

                        내용 @@@@@@@@@
                        @@@@@@@@@@@@@
                        @@@@@@@@@@@@@

                        """)
            
            st.info("""
                    파란 블럭 창~
                    """)
            
            st.markdown("""
                        마크 다운 내용~~~
                        """)
    # 사이드바 메뉴
    if st.sidebar.button("공모전"):
        st.session_state["page"] = "competition"
        st.rerun()

    if st.sidebar.button("스터디 바로가기"):
        st.session_state["page"] = "study"
        st.rerun()

    if st.sidebar.button("동아리 바로가기"):
        st.session_state["page"] = "club"
        st.rerun()

    if st.sidebar.button("팀원 모집 바로가기"):
        st.session_state["page"] = "recruitment"
        st.rerun()

    if st.sidebar.button("자유 게시판 바로가기"):
        st.session_state["page"] = "board"
        st.rerun()

# 페이지 전환
elif page == "competition":
    exec(open("competition.py").read())
elif page == "study":
    exec(open("study.py").read())
elif page == "club":
    exec(open("club.py").read())
elif page == "recruitment":
    exec(open("recruitment.py").read())
elif page == "board":
    exec(open("board.py").read())