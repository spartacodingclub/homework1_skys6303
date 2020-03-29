import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('tr.list')
movies1 = movies[0]
title = movies1.select('a.title.ellipsis')[0].text
artist = movies1.select('a.artist.ellipsis')[0].text


# movies (tr들) 의 반복문을 돌리기
rank = 1
for movies1 in movies:
    title = movies1.select('a.title.ellipsis')[0].text
    artist = movies1.select('a.artist.ellipsis')[0].text
    print(rank, title.strip(), artist.strip())
    rank += 1