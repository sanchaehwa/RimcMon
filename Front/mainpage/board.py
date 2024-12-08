import streamlit as st

st.title("게시판")
st.write("여기는 자유 게시판 streamlit파일.")

if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
    st.rerun()
