import requests

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/truncate_crawl_data.php"

try:
    response = requests.get(url)    # GET 요청 보내기
    if response.status_code == 200: # 응답 상태 확인
        print("PHP 응답:")
        print(response.text)      # 응답 확인
    else:
        print(f"PHP 응답 오류: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"HTTP 요청 중 오류 발생: {e}")
