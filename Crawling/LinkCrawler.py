import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs
import time

def init_driver():
    driver = webdriver.Chrome()
    return driver

# 이벤트 ID 리스트 추출
def extract_event_ids(driver, main_url, pages=2):
    event_ids = []

    for page in range(1, pages + 1):  # 1페이지부터 `pages`까지 크롤링
        driver.get(f"{main_url}&page={page}")  # 페이지 쿼리 추가
        try:
            # 이벤트 ID를 포함한 링크 추출
            event_links = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "#content > div > section.event_main_area > ul li article.event_area.event_main a, "
                                      "#content > div > section.event_main_area > ul li article.event_area.event_main.adv_list a")
                )
            )
            # URL 파싱을 통해 이벤트 ID 추출
            for link in event_links:
                href = link.get_attribute("href")
                parsed_url = urlparse(href)
                if 'event' in parsed_url.path:
                    event_id = parsed_url.path.split('/')[-1]
                    event_ids.append(event_id)
                elif 'url' in parse_qs(parsed_url.query):
                    # 쿼리 매개변수를 사용하여 이벤트 ID 추출
                    event_id = parse_qs(parsed_url.query)['url'][0].split('/')[-1]
                    event_ids.append(event_id)
        except Exception as e:
            print(f"{page}페이지 이벤트 ID 추출 오류:", e)
        time.sleep(2)  # 페이지 로딩 대기
    return event_ids

# 모집 페이지 경로 추출
def extract_recruitment_page(driver, event_url):
    driver.get(event_url)
    try:
        # 참여 신청이 마감된 이벤트 확인
        closed_message = driver.find_elements(By.CSS_SELECTOR, "#content > div.content_wrapping.wide_max_width_area > section.event_summary > div.right_area > form > div.btn_area > span")
        if closed_message and "참여 신청이 마감되었습니다" in closed_message[0].text:
            return "참여 신청 마감"

        # "신청하기" 버튼 처리
        apply_button = driver.find_elements(By.CSS_SELECTOR, "#content > div.content_wrapping.wide_max_width_area > section.event_summary > div.right_area > form > div.btn_area > input")
        if apply_button and "신청하기" in apply_button[0].get_attribute("value"):
            return event_url  # 현재 페이지를 모집 페이지로 반환

        # 모집 페이지 링크 추출
        recruitment_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#content > div.content_wrapping.wide_max_width_area > section.event_summary > div.right_area > form > div.btn_area > a")
            )
        )
        return recruitment_link.get_attribute("href")
    except Exception as e:
        print(e)
    return None

# 공모전 모집 페이지 경로를 반환하는 함수
def get_link_data():
    base_url = "https://onoffmix.com/event/main/?c=105"
    driver = init_driver()

    try:
        # 1. 카테고리가 '공모전'인 모든 이벤트 ID 추출 (2페이지 크롤링)
        event_ids = extract_event_ids(driver, base_url, pages=2)
        recruitment_data = []

        if event_ids:
            # 2. 각 이벤트 ID에 대해 실제 모집 페이지 경로 추출
            for event_id in event_ids:
                event_url = f"https://www.onoffmix.com/event/{event_id}"
                recruitment_page = extract_recruitment_page(driver, event_url)
                recruitment_data.append({"event_id": event_id, "recruitment_page": recruitment_page})

            # JSON 형태로 결과 반환
            return json.dumps(recruitment_data, ensure_ascii=False, indent=4)
        else:
            return json.dumps({"error": "이벤트 ID를 추출할 수 없습니다."}, ensure_ascii=False, indent=4)
    finally:
        driver.quit()

# data = get_link_data()
# print(data)