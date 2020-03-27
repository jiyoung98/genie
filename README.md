# 3주차 과제: genie

## 결과물

---
```

1 WANNABE ITZY (있지)
2 어떻게 지내 오반
3 아무노래 지코 (ZICO)
4 시작 가호 (Gaho)
5 ON 방탄소년단
6 마음을 드려요 아이유 (IU)
7 METEOR 창모 (CHANGMO)
8 바빠서 (Feat. 헤이즈) 개코
9 FIESTA IZ*ONE (아이즈원)
10 Blueming 아이유 (IU)
...
48 사랑에 연습이 있었다면 (Prod. by 2soo) 임재현
49 포장마차 황인욱
50 사랑이 식었다고 말해도 돼 먼데이 키즈 (Monday Kiz)

```

## 문제점

---

> ### 1. 공백이 함께 출력되는 문제
>
> > 수업 시간에 배운대로 .string 으로 문자열만 뽑아냈지만, 원하는 데이터 외에도 공백이 너무 많이 출력되는 오류가 있었다. 출력할때 공백을 제거하는 .strip() 함수로 문제를 해결했다.

```python

rank = 1
list = soup.select('td.info')
for item in list:
    title = item.select_one('a.title')
    artist = item.select_one('a.artist')
    print(rank, title.string.strip(), artist.string.strip())
    rank += 1

```