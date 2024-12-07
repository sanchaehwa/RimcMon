import streamlit as st

st.title("팀원 모집")
st.write("여기는 팀원 모집 streamlit파일.")

if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
