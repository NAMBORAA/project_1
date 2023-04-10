import requests
from bs4 import BeautifulSoup
import re

url ="https://www.airbnb.co.kr/s/%EC%A0%9C%EC%A3%BC%EB%8F%84/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&search_type=filter_change&date_picker_type=calendar&checkin=2022-12-07&checkout=2022-12-15&source=structured_search_input_header"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
a = soup.select(" div.g1qv1ctd.cb4nyux.dir.dir-ltr > span")
b = soup.select("div.c1l1h97y.dir.dir-ltr > div > meta[itemprop='content']")   #url 뽑아

list3 = []
for i in b:
    list3.append(i.text())

print(list3)
