import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) + '/..')))
from Python_Script_Profile.insert_to_db import get_user_data

user_data = get_user_data()

# 각 사용자 데이터의 'tool' 부분을 출력
for user in user_data:
    # tool 부분을 마크다운 형식으로 출력
    st.markdown(f"**Tool Badge for {user['name']}:**")
    st.markdown(f'<img src="{user["tool"]}" alt="Tool Badge" style="max-width: 100%; height: auto;">', unsafe_allow_html=True)