from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import time

def get_contest_data():
    driver = webdriver.Chrome()
    url = 'https://onoffmix.com/event/main/?c=105'
    driver.get(url)

    contest_data = []

    for page in range(1, 3):  # 크롤링할 페이지 범위 (1페이지부터 2페이지까지)
        try:
            # 공모전 리스트 로딩 대기
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li')))

            # 데이터 요소 가져오기
            images = driver.find_elements(By.CSS_SELECTOR, '#content > div > section.event_main_area > ul img')
            titles = driver.find_elements(By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li article.event_area.event_main a div.event_info_area div.title_area')
            dates = driver.find_elements(By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li article.event_area.event_main a div.event_info_area div.event_info div.date')

            # 데이터 전처리
            for img, title, date in zip(images, titles, dates):
                img_url = img.get_attribute("src")
                full_title = title.text
                date_info = date.text.strip()
                if full_title.startswith("["):
                    full_title = re.sub(r'\[.*?\]', '', full_title).strip()

                contest_data.append({
                    "title": full_title,
                    "image": img_url,
                    "date": date_info,
                })

            # 다음 페이지로 이동
            if page < 2:  # 마지막 페이지에서는 버튼을 클릭하지 않음
                next_button = driver.find_element(By.CSS_SELECTOR, 
                    "#content > div > section.event_main_area > div.pagination_wrap > div > a:nth-child(3)")
                next_button.click()

                # 페이지 로딩 대기
                time.sleep(3)

        except Exception as e:
            print(f"{page}페이지 크롤링 중 오류:", e)
            break

    driver.quit()
    return contest_data

# # 데이터 크롤링 결과
# data = get_contest_data()

# # JSON 형식으로 출력
# crwaling_data = json.dumps(data, ensure_ascii=False, indent=4)
# print(crwaling_data)