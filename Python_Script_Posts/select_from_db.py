import requests

# 특정 카테고리의 게시글 조회
def get_posts_by_category(category):
    url = "http://opsw4.dothome.co.kr/select_from_post_data.php"  

    try:
        params = {'category': category} 
        response = requests.get(url, params=params)

        if response.status_code == 200:
            try:
                data = response.json()  
                return data 
            except ValueError:
                raise ValueError("JSON 응답 파싱 실패")
        else:
            raise Exception(f"요청 실패: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"요청 중 오류 발생: {e}")

# 특정 ID의 게시글 조회
def get_post_by_id(post_id):
    url = "http://opsw4.dothome.co.kr/select_from_post_data.php" 

    try:
        params = {'id': post_id} 
        response = requests.get(url, params=params)

        if response.status_code == 200:
            try:
                data = response.json()
                if data and len(data) > 0:
                    return data[0]  # 첫 번째 게시글 반환 (ID는 고유값이므로 하나만 반환됨)
                else:
                    return None  
            except ValueError:
                raise ValueError("JSON 응답 파싱 실패")
        else:
            raise Exception(f"요청 실패: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"요청 중 오류 발생: {e}")