from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json

def get_contest_data():
    driver = webdriver.Chrome()
    url = 'https://www.onoffmix.com/event/main?s=공모전'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li article.event_area.event_main a div.event_info_area div.title_area')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li article.event_area.event_main a div.event_info_area div.event_info div.date')))
    except Exception as e:
        print("페이지 로딩 중 오류:", e)
        driver.quit()
        return []

    # 실제 공모전 데이터 (포스터, 제목, 날짜)
    images = driver.find_elements(By.CSS_SELECTOR, '#content > div > section.event_main_area > ul img')
    titles = driver.find_elements(By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li article.event_area.event_main a div.event_info_area div.title_area')
    dates = driver.find_elements(By.CSS_SELECTOR, '#content > div > section.event_main_area > ul > li article.event_area.event_main a div.event_info_area div.event_info div.date')

    contest_data = []

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
            "date": date_info
        })

    driver.quit()
    return contest_data

# # 데이터 크롤링 결과
# data = get_contest_data()

# # json 형식으로 formatting
# crwaling_data = json.dumps(data, ensure_ascii=False, indent=4)

# print(crwaling_data)