from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium
import time
from bs4 import BeautifulSoup
from time import sleep
import random
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
from selenium.webdriver.common.keys import Keys


def scroll(modal, driver):
    try:
        # 스크롤 높이 받아오기
        last_height = driver.execute_script("return arguments[0].scrollHeight", modal)
        while True:
            pause_time = random.uniform(0.5, 0.8)
            # 최하단까지 스크롤
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", modal)
            # 페이지 로딩 대기
            time.sleep(pause_time)
            # 무한 스크롤 동작을 위해 살짝 위로 스크롤
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight-50);", modal)
            time.sleep(pause_time)
            # 스크롤 높이 새롭게 받아오기
            new_height = driver.execute_script("return arguments[0].scrollHeight", modal)

            # 스크롤 완료 경우
            if new_height == last_height:
                print("스크롤 완료")
                break
            last_height = new_height

    except Exception as e:
        print("에러 발생: ", e)


driver = webdriver.Chrome('chromedriver')
url = "https://www.airbnb.co.kr/rooms/35685915?adults=1&category_tag=Tag%3A8536&children=0&infants=0&search_mode=flex_destinations_search&check_in=2022-12-04&check_out=2022-12-09&federated_search_id=701bee68-ff09-4e0e-ab34-a62e0f4f6d4e&source_impression_id=p3_1667541158_Ky3ZBSQgqHvBQ6yv"
driver.get(url)
wait = WebDriverWait(driver, 2)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ' div.stu4mdj.dir.dir-ltr > button').click()
all_review_page = "/html/body/div[9]/section/div/div/div[2]/div"
page_loading_wait = wait.until(EC.element_to_be_clickable((By.XPATH, all_review_page)))
modal = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_17itzz4']")))
scroll(modal, driver)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reveiw = soup.select("span.ll4r2nl.dir.dir-ltr")[1:]

for i in reveiw:
    print(i.text)