import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) + '/..')))
from Python_Script.select_from_db import get_mysql_data

# 데이터를 가져와서 Streamlit에 표시하기
def display_data():
    data = get_mysql_data()


    # CSS 스타일 추가
    st.markdown(
        """
        <style>
        .card {
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            padding: 20px;
            margin: 10px 0;
        }
        .card img {
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .card-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
            color: #333;
        }
        .card-info {
            font-size: 1rem;
            margin-bottom: 5px;
            color: #555;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 데이터가 있으면 Streamlit을 통해 출력
    if data:
        for row in data:
            st.markdown(
            f"""
            <div class="card">
                <img src="{row['image']}" alt="Image">
                <div class="card-title">{row['title']}</div>
                <div class="card-info"><strong>ID:</strong> {row['id']}</div>
                <div class="card-info"><strong>Date:</strong> {row['date']}</div>
            </div>
            """,
            unsafe_allow_html=True
)

    else:
        st.write("No data found!")

# Streamlit 앱 실행
if __name__ == "__main__":
    st.title("MySQL Data Rendering Sample")
    display_data()
