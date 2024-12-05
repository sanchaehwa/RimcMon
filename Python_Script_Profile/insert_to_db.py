import logging
import requests

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/insert_into_user_data.php"

# 데이터 전송 함수
def send_data_to_server(data):
    params = {
        "name": data['name'],
        "bio": data['bio'],
        "tool": data['tools'],
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("응답 성공:", response.text)
    else:
        print("요청 실패:", response.status_code)

# 데이터 합치기 (JSON 반환)
def combine_data_for_db(skills, session_state):
    return {
        "name": session_state.name.strip(),
        "bio": session_state.self_intro.strip(),
        "tools": [skills[skill] for skill in session_state.selected_skills],
    }

