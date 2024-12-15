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
                        대학생을 위한 리크루팅 서비스 림크몬

                        """)
            
            st.info("""
                    대학생을 위한 프로젝트 / 공모전 등의 매칭 서비스를 제공하는 림크몬 👾 개발 저장소입니다.
                    림크몬은 대학생이 자신의 관심사와 전공 등 역량에 맞는 활동에 참여할 수 있도록 돕는 매칭 서비스입니다.
                    다양한 활동을 통해 자신의 역량을 성장시키고, 새로운 기회를 발견하는 것을 목표로 합니다.
                    """)
        
    # 사이드바 메뉴
    if st.sidebar.button("로그인"):
        st.session_state["page"] = "user"
        st.rerun()
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
elif page == "user":
    exec(open("../profilepage/user.py").read())
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