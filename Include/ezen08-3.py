'''
    * 웹 크롤링
      - 날짜 추출
        - tb 태그중에 원하는 정보만을 따로 가져와야 함
        - 날짜 태그 규칙 찾아서 td태그들 중에 날짜를 가져옴


'''

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"

import requests
source = requests.get(page_url).text

import bs4
source = bs4.BeautifulSoup(source)

dates = source.find_all('td', class_ = 'date')

date_list = []

# 날짜 크롤링
for date in dates:
  date_list.append(date.text)

# 체결가 추출
prices = source.find_all('td', class_ = 'number_1')
price_list = []
prices = prices[::4]
for price in prices:
  price_list.append(price.text)
print(price_list)

prices2 = source.find_all('td', class_ = 'number_1')
price_list2 = []
for price in prices2[::4]:
  price_list2.append(price.text)
print(price_list2)
print(len(date_list))
print(len(price_list2))

#/html/body/div/table[2]/tbody/tr/td[11]/a
result = source.find_all("td", class_="pgRR")[0]
#print(result)

last_url = source.find_all("td", class_="pgRR")[0].find_all('a')[0]["href"]
#print(last_url)

result = last_url.split('&page=')
#print(result)

last_page = last_url.split('&page=')[-1]
#print(last_page)

# 마지막 페이지 번호 찾기
last_page = int(last_url.split('&page=')[-1])
print(last_page)