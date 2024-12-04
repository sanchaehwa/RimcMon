import requests
import sys
import os
# 현재 파일의 상위 디렉토리를 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
# from Profile_FE.profile import get_user_data

def get_user_data():
    return [
        {"name": "John Doe", "bio": "Developer", "tool": "https://img.shields.io/badge/Adobe Photoshop-31A8FF?style=flat-square&logo=Adobe Photoshop&logoColor=white"},
        {"name": "Jane Smith", "bio": "Designer", "tool": "https://img.shields.io/badge/Adobe Illustrator-FF9A00?style=flat-square&logo=Adobe Illustrator&logoColor=white"}
    ]

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/insert_into_user_data.php"

for i in get_user_data():
    params = { # GET 요청의 쿼리 파라미터
        # 데이터 포맷
        "name": i['name'],
        "bio": i['bio'],
        "tool": i['tool'],
    }

    # GET 요청 보내기
    response = requests.get(url, params=params)

    # 응답 출력
    if response.status_code == 200:
        print("응답 성공:", response.text)
    else:
        print("요청 실패:", response.status_code)
