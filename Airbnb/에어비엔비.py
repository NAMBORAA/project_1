import requests
from bs4 import BeautifulSoup
import re

url ="https://www.airbnb.co.kr/s/%EC%A0%9C%EC%A3%BC%EB%8F%84/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&search_type=filter_change&date_picker_type=calendar&checkin=2022-12-07&checkout=2022-12-15&source=structured_search_input_header"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
a = soup.select(" div.g1qv1ctd.cb4nyux.dir.dir-ltr > span")
b = soup.select("div.c1l1h97y.dir.dir-ltr >  div > meta[itemprop='content']")   #url 뽑아

# a - 별점, 후기 들어있는 정보, 후기 개수 추출
list1=[]
for i in a:
    list1.append(i.text)

print(list1)

# 후기가 없는 NEW 값 --> 0으로 대체
for i in list1:
    if i == 'NEW':
        new_index = list1.index('NEW')
        list1[new_index] = '(0)'
print(list1)


# 괄호안의 글씨 가져오기
import re
# str ="LOG_ADD(LOG_FLOAT, actuatorThrust, &actuatorThrust)"
# items = re.findall('\(([^)]+)', list1)   #extracts string in bracket()
# print(items)

list2=[]
for i in list1:
    items = re.findall('\(([^)]+)', i)   #extracts string in bracket()
    list2.append(items)

print(list2)