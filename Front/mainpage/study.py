import streamlit as st

# 초기 상태 설정
if "study_posts" not in st.session_state:
    st.session_state["study_posts"] = []  # 게시글 리스트

# 페이지 타이틀
st.title("📘 스터디 게시판")
st.write("여기는 스터디 게시판입니다. 게시글을 등록하고 확인할 수 있습니다.")

# 게시글 등록 섹션
st.header("📄 게시글 등록")
with st.form("study_form", clear_on_submit=True):
    title = st.text_input("제목", placeholder="스터디 제목을 입력하세요.")
    content = st.text_area("내용", placeholder="스터디 내용을 입력하세요.")
    submit_button = st.form_submit_button("등록하기")

    if submit_button:
        if title and content:
            st.session_state["study_posts"].append({"title": title, "content": content})
            st.success("게시글이 성공적으로 등록되었습니다!")
        else:
            st.error("제목과 내용을 모두 입력해주세요.")

# 게시글 확인 섹션
st.header("📋 게시글 목록")
if st.session_state["study_posts"]:
    for idx, post in enumerate(st.session_state["study_posts"]):
        with st.expander(f"{idx + 1}. {post['title']}"):
            st.write(post['content'])
else:
    st.info("등록된 게시글이 없습니다.")

# 메인 페이지로 돌아가는 버튼
if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
    st.rerun()
