'''
    * 웹 크롤링
      - 날짜 추출
        - tb 태그중에 원하는 정보만을 따로 가져와야 함
        - 날짜 태그 규칙 찾아서 td태그들 중에 날짜를 가져옴


'''

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
#print(page_url)

import requests
source = requests.get(page_url).text

import bs4
source = bs4.BeautifulSoup(source)

dates = source.find_all('td', class_ = 'date')
#print(result)
#print(dates)
#print(dates[0])
#print(dates[0].text)

date_list = []

# 날짜 크롤링
for date in dates:
  date_list.append(date.text)

#print(date_list)

# 체결가 추출
prices = source.find_all('td', class_ = 'number_1')
price_list = []
prices = prices[::4]
'''
    체결가 변동량(천주) 거래량(천주) 거래대금(백만) 들도 같은 태그(number_1)를 공유하고 있어
    4개씩 증가하는 것을 알 수 있음
    4의 배수로 건너뛰면서 추출하면 바로 체결가만 가져올 수 있음
'''
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