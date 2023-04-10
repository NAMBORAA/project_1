# dict_url = {}
#
#
# def collect_url(region):
#     url = f'https://www.airbnb.co.kr/s/{region}/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&source=structured_search_input_header&search_type=search_query'
#     driver = webdriver.Chrome('chromedriver')
#     driver.get(url)
#     time.sleep(2)
#     html = driver.page_source  # 현재 페이지 소스로
#     soup = BeautifulSoup(html, 'html.parser')  # 파싱
#
#     b = soup.select("div.c1l1h97y.dir.dir-ltr >  div > meta[content]")  # url 뽑아
#     a = []  # url
#     c = []  # 가격
#     for i in range(len([str(x) for x in [x for x in b][2::3]])):  # 지역명_url에 append
#         try:
#             if len([x for x in soup.select('span.r1dxllyb.dir.dir-ltr')[i].text.split()[-1] if x.isdigit()]) <= 2:
#                 pass
#             else:
#                 a.append('https://' + [str(x) for x in [x for x in b][2::3]][i][15:-18])
#                 c.append(int(''.join(
#                     [x for x in soup.select('div.p11pu8yw.dir.dir-ltr')[i].text.split()[0] if x.isdigit()])))
#                 i + 1
#         except:
#             pass
#     # 넘겨야 할 페이지 수
#     leng = ''.join([i for i in soup.select(
#         '#site-content > div.fhusglq.dir.dir-ltr > div.p1lc3mon.dir.dir-ltr > div > div > div > div > section > h1 > span')[
#         0].text if i.isdigit() == True])
#     length = 0
#     if int(leng) >= 300:
#         length += 15
#     elif int(leng) % 20 != 0:
#         length += int(leng) // 20 + 1
#
#     if length <= 7:  # 페이지 수가 7페이지 이하라면
#         for j in range(1, length):
#             driver.find_element(By.CSS_SELECTOR,
#                                 f'#site-content > div.fhusglq.dir.dir-ltr > div:nth-child(4) > div > div > nav > div > a:nth-child({j + 2})').click()
#             time.sleep(2)
#             html = driver.page_source  # 현재 페이지 소스로
#             soup = BeautifulSoup(html, 'html.parser')
#             b = soup.select("div.c1l1h97y.dir.dir-ltr >  div > meta[content]")  # url 주소 뽑아서
#             for i in range(len([str(x) for x in [x for x in b][2::3]])):  # 지역명_url에 append
#                 a.append('https://' + [str(x) for x in [x for x in b][2::3]][i][15:-18])
#                 c.append(int(''.join(
#                     [x for x in soup.select('div.p11pu8yw.dir.dir-ltr')[i].text.split()[0] if x.isdigit()])))
#
#     else:
#         for i in range(1, length):
#             if i <= 3:  # 2,3,4 번 페이지 클릭
#                 driver.find_element(By.CSS_SELECTOR,
#                                     f'#site-content > div.fhusglq.dir.dir-ltr > div:nth-child(4) > div > div > nav > div > a:nth-child({i + 2})').click()
#                 time.sleep(2)
#                 html = driver.page_source  # 현재 페이지 소스로
#                 soup = BeautifulSoup(html, 'html.parser')
#                 b = soup.select("div.c1l1h97y.dir.dir-ltr >  div > meta[content]")  # url 뽑아
#                 for i in range(len([str(x) for x in [x for x in b][2::3]])):  # 지역명_url에 append
#                     a.append('https://' + [str(x) for x in [x for x in b][2::3]][i][15:-18])
#                     c.append(int(''.join(
#                         [x for x in soup.select('div.p11pu8yw.dir.dir-ltr')[i].text.split()[0] if x.isdigit()])))
#
#             elif 4 <= i <= length - 2:  # 5,6,7,8,9,10,11 번 페이지 클릭
#                 driver.find_element(By.CSS_SELECTOR,
#                                     '#site-content > div.fhusglq.dir.dir-ltr > div:nth-child(4) > div > div > nav > div > a:nth-child(6)').click()
#                 time.sleep(2)
#                 html = driver.page_source  # 현재 페이지 소스로
#                 soup = BeautifulSoup(html, 'html.parser')
#                 b = soup.select("div.c1l1h97y.dir.dir-ltr >  div > meta[content]")  # url 주소 뽑아서
#                 for i in range(len([str(x) for x in [x for x in b][2::3]])):  # 지역명_url에 append
#                     a.append('https://' + [str(x) for x in [x for x in b][2::3]][i][15:-18])
#                     c.append(int(''.join(
#                         [x for x in soup.select('div.p11pu8yw.dir.dir-ltr')[i].text.split()[0] if x.isdigit()])))
#
#             else:  # 마지막 페이지 클릭
#                 driver.find_element(By.CSS_SELECTOR,
#                                     '#site-content > div.fhusglq.dir.dir-ltr > div:nth-child(4) > div > div > nav > div > a:nth-child(7)').click()
#                 time.sleep(2)
#                 html = driver.page_source  # 현재 페이지 소스로
#                 soup = BeautifulSoup(html, 'html.parser')
#                 b = soup.select("div.c1l1h97y.dir.dir-ltr >  div > meta[content]")  # url 주소 뽑아서
#                 for i in range(len([str(x) for x in [x for x in b][2::3]])):  # 지역명_url에 append
#                     a.append('https://' + [str(x) for x in [x for x in b][2::3]][i][15:-18])
#                     c.append(int(''.join(
#                         [x for x in soup.select('div.p11pu8yw.dir.dir-ltr')[i].text.split()[0] if x.isdigit()])))
#     dict_url[f'{region}'] = list(zip(a, c))


###################################################
#이미지 크롤링

#라이브러리 불러오기
from selenium import webdriver
import time
from urllib.request import urlopen, urlparse, urlunparse, urlretrieve
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium
import time
from bs4 import BeautifulSoup
from time import sleep
import random
# import pandas as pd
import warnings

url = f'https://www.airbnb.co.kr/s/서울특별시/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&source=structured_search_input_header&search_type=search_query'
driver = webdriver.Chrome('chromedriver')
driver.get(url)
time.sleep(2)
html = driver.page_source  # 현재 페이지 소스로
soup = BeautifulSoup(html, 'html.parser')  # 파싱

'''이미지 src요소를 리스트업해서 이미지 url 저장'''

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")  # 클래스 네임에서 공백은 .을 찍어줌
images_url = []
for i in images:

    if i.get_attribute('src') != None:
        images_url.append(i.get_attribute('src'))
    else:
        images_url.append(i.get_attribute('data-src'))
driver.close()

# 겹치는 이미지 url 제거

print("전체 다운로드한 이미지 개수: {}\n동일한 이미지를 제거한 이미지 개수: {}".format(len(images_url), len(pd.DataFrame(images_url)[0].unique())))
images_url = pd.DataFrame(images_url)[0].unique()


#'''해당하는 파일에 이미지 다운로드'''
#
#if image_name == 'shark' :
#   for t, url in enumerate(images_url, 0):
#      urlretrieve(url, shark + image_name + '_' + str(t) + '.jpg')
#   driver.close()
#
#elif image_name == 'whale' :
#   for t, url in enumerate(images_url, 0):
#      urlretrieve(url, whale + image_name + '_' + str(t) + '.jpg')
#   driver.close()
#
#elif image_name == 'dolphin' :
#   for t, url in enumerate(images_url, 0):
#      urlretrieve(url, dolphin + image_name + '_' + str(t) + '.jpg')
#   driver.close()

