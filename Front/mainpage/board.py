import streamlit as st
from datetime import datetime

# 스타일 적용
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa; /* 배경 색 */
    }
    .title {
        color: #007BFF; /* 제목 색상 */
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .post {
        border: 1px solid #dee2e6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        background-color: white;
    }
    .post-title {
        font-size: 1.25rem;
        font-weight: bold;
        color: #343a40;
    }
    .post-content {
        font-size: 1rem;
        color: #495057;
        margin-top: 10px;
    }
    .post-author {
        font-size: 0.9rem;
        color: #868e96;
        text-align: right;
        margin-top: 15px;
    }
    .form-container {
        border: 1px solid #dee2e6;
        padding: 15px;
        border-radius: 10px;
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 페이지 제목
st.markdown('<div class="title">자유 게시판</div>', unsafe_allow_html=True)

# 게시판 데이터 저장소 (임시)
if "posts" not in st.session_state:
    st.session_state["posts"] = []


with st.expander("### 게시글 목록"):

    if st.session_state["posts"]:
        for post in st.session_state["posts"]:
            st.markdown('<div class="post">', unsafe_allow_html=True)
            st.markdown(f'<div class="post-title">{post["title"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="post-content">{post["content"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="post-author">- {post["author"]} ({post["timestamp"]})</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("아직 작성된 글이 없습니다. 첫 번째 글을 작성해보세요!")

# 게시판 글 작성
with st.expander("** 등록 **"):
    with st.container():
        # st.markdown('<div class="form-container">', unsafe_allow_html=True)
        title = st.text_input("제목", placeholder="글 제목을 입력하세요.")
        content = st.text_area("내용", placeholder="글 내용을 입력하세요.")
        author = st.text_input("작성자", placeholder="작성자의 이름을 입력하세요.")
        submit = st.button("작성하기")

        if submit:
            if title and content and author:
                new_post = {
                    "title": title,
                    "content": content,
                    "author": author,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                }
                st.session_state["posts"].insert(0, new_post)  # 최신 글이 위로 오도록
                st.success("글이 성공적으로 작성되었습니다!")
            else:
                st.error("모든 필드를 작성해주세요.")
        st.markdown("</div>", unsafe_allow_html=True)

# 게시판 글 목록
if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
    st.rerun()
