import requests

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/insert_into_crawl_data.php"
params = { # GET 요청의 쿼리 파라미터
    # 데이터 포맷
    "title": "제목 데이터",
    "date": "내용 ~~~",
    "image": "https://img2.stibee.com/36150_2328124_1723012489158038678.PNG",    
}

# GET 요청 보내기
response = requests.get(url, params=params)

# 응답 출력
if response.status_code == 200:
    print("응답 성공:", response.text)
else:
    print("요청 실패:", response.status_code)
