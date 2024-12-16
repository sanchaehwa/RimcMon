import requests
import sys
import os
import json

# 현재 파일의 상위 디렉토리를 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from Crawling.Crawler import get_contest_data
from Crawling.LinkCrawler import get_link_data


def insert_mysql_data():
    # 요청을 보낼 URL
    url = "http://opsw4.dothome.co.kr/insert_into_crawl_data.php"

    # 공모전 데이터 가져오기
    contest_data = get_contest_data()

    # 모집 페이지 데이터 가져오기
    link_data = json.loads(get_link_data())  # JSON 문자열을 Python 객체로 변환

    # 모집 페이지 데이터를 `contest_data`에 병합
    for idx, contest in enumerate(contest_data):
        # 모집 페이지가 존재하면 병합, 없으면 기본값 설정
        contest["page"] = link_data[idx]["recruitment_page"] if idx < len(link_data) else "N/A"

        # GET 요청의 쿼리 파라미터
        params = {
            "title": contest['title'],
            "date": contest['date'],
            "image": contest['image'],
            "page": contest['page'],  # 추가된 page 데이터
        }

        # GET 요청 보내기
        response = requests.get(url, params=params)

        # 응답 출력
        if response.status_code == 200:
            print("응답 성공:", response.text)
        else:
            print("요청 실패:", response.status_code)