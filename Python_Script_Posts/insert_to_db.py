import logging
import requests

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/insert_into_post_data.php"

# 프론트에서 넘어오는 실제 게시글 데이터 예시
# data = {
#     'title': '스터디 모집 공고',
#     'content': '스터디 참여자를 모집합니다.',
#     'author': '김진범',
#     'category': 'study'
# }

def insert_post_data(data):
    params = {
        "title": data['title'],
        "content": data['content'],
        "author": data['author'],
        "category": data['category']
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            logging.info("게시글 삽입 성공: %s", response.text)
        else:
            logging.error("게시글 삽입 요청 실패: %s", response.status_code)
    except requests.exceptions.RequestException as e:
        logging.error("요청 중 오류 발생: %s", e)
