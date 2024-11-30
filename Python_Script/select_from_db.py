import requests

def get_mysql_data():
    url = "http://opsw4.dothome.co.kr/select_from_crawl_data.php" # PHP API URL

    try:
        # GET 요청 보내기
        response = requests.get(url)
        
        # 응답 상태 확인
        if response.status_code == 200:
            # JSON 데이터 파싱
            data = response.json()
            # 출력 코드
            # for item in data:
            #     print(f"ID: {item['id']}\n Title: {item['title']}\n Date: {item['date']}\n Image: {item['image']}\n\n")
        else:
            print(f"요청 실패: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")

    return data
