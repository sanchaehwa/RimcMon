import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from Python_Script_Posts.insert_to_db import insert_post_data
from Python_Script_Posts.select_from_db import get_post_by_id, get_posts_by_category

# Streamlit UI 구성
st.title("게시판 관리 시스템")

# 사이드바 카테고리 선택
category = st.sidebar.radio("카테고리 선택", ["study", "recruit", "other"], key="category_radio")

# 게시글 목록 및 등록
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "list"  # 기본 뷰 모드: 목록 보기

if st.session_state.view_mode == "list":
    # 카테고리별 게시글 목록 조회
    st.header(f"{category} 게시글 목록")
    posts = get_posts_by_category(category)

    if posts:
        for post in posts:
            if st.button(f"게시글: {post['title']}", key=f"post_button_{post['id']}"):  # 고유 key 추가
                st.session_state["post_id"] = post["id"]
                st.session_state.view_mode = "detail"  # 상세보기 모드로 전환
                st.rerun()
    else:
        st.warning("현재 카테고리에 게시글이 없습니다.")

    # 게시글 등록 버튼
    if st.button("게시글 등록", key="register_button"):
        st.session_state.view_mode = "register"  # 등록 모드로 전환
        st.rerun()

elif st.session_state.view_mode == "register":
    # 게시글 등록 UI
    st.header("게시글 등록")
    title = st.text_input("제목")
    content = st.text_area("내용")
    author = st.text_input("작성자")
    selected_category = st.radio("카테고리 선택", ["study", "recruit", "other"], 
                                 index=["study", "recruit", "other"].index(category), 
                                 key="category_radio_register")

    if st.button("등록", key="submit_button"):
        if title and content and author:
            data = {
                "title": title,
                "content": content,
                "author": author,
                "category": selected_category
            }
            insert_post_data(data)
            st.success("게시글이 등록되었습니다.")
            st.session_state.view_mode = "list"  # 등록 후 목록 보기로 전환
            st.rerun()
        else:
            st.error("모든 필드를 입력해주세요.")

    if st.button("취소", key="cancel_button"):
        st.session_state.view_mode = "list"  # 목록 보기로 전환
        st.rerun()

elif st.session_state.view_mode == "detail":
    # 특정 게시글 조회
    post_id = st.session_state["post_id"]
    post = get_post_by_id(post_id)

    if post:
        st.subheader(post["title"])
        st.write(f"작성자: {post['author']}, 카테고리: {post['category']}")
        st.write(f"내용: {post['content']}")
    else:
        st.warning("해당 게시글을 찾을 수 없습니다.")

    if st.button("목록으로 돌아가기", key="back_to_list_button"):
        st.session_state.view_mode = "list"
        st.rerun()