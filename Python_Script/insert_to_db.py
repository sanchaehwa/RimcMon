import requests
import sys
import os
# 현재 파일의 상위 디렉토리를 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from Crawling.Crawler import get_contest_data

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/insert_into_crawl_data.php"

for i in get_contest_data():
    params = { # GET 요청의 쿼리 파라미터
        # 데이터 포맷
        "title": i['title'],
        "date": i['date'],
        "image": i['image'],
    }

    # GET 요청 보내기
    response = requests.get(url, params=params)

    # 응답 출력
    if response.status_code == 200:
        print("응답 성공:", response.text)
    else:
        print("요청 실패:", response.status_code)
