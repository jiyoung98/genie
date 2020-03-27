import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

rank = 1
list = soup.select('td.info')
for item in list:
    title = item.select_one('a.title')
    artist = item.select_one('a.artist')
    print(rank, title.string.strip(), artist.string.strip())
    rank += 1