import streamlit as st

# 초기 상태 설정
if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []  # 업로드된 파일 목록을 저장하는 리스트

st.title("동아리 게시판")

# 파일 업로드 섹션
st.header("📂 파일 업로드")
uploaded_files = st.file_uploader("파일을 업로드하세요.", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # 업로드된 파일을 세션 상태에 추가
        st.session_state["uploaded_files"].append(uploaded_file)

# 업로드된 파일 리스트 표시
st.subheader("업로드된 파일 목록")
if st.session_state["uploaded_files"]:
    for idx, file in enumerate(st.session_state["uploaded_files"]):
        st.write(f"{idx + 1}. **{file.name}**")
else:
    st.info("아직 업로드된 파일이 없습니다.")

# 메인 페이지로 돌아가는 버튼
if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
