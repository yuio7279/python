from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen , Request
import pandas as pd

menuList = []
nameList = []
rankList = []
priceList = []
urlList = []

try:
    urlTicker = Request('https://www.chicagomag.com/chicago-magazine/november-2020/sandwich-city/the-10-best-sandwiches/', headers={'User-Agent':'Mozilla/5.0'})
    readTicker = urlopen(urlTicker)
    soup = bs(readTicker, 'html.parser')
    
    for link in soup.find_all('figcaption'):               
        try:
            menuList.append(link.find('strong').getText())   #메뉴 가져오는 부분입니다

            h2 = (link.findAll('h2'))                        
            rankList.append(h2[0].getText())                 #랭킹 가져오는 부분입니다
            nameList.append(h2[1].getText())                 #매장명 가져오는 부분입니다.

        except AttributeError:
            continue                                         



    for em in soup.findAll('em'):
        try:
            s_string = em.getText().split()
            addr = s_string[1]+' '+s_string[2]+' '+s_string[3]+' '+s_string[4]
            
            addr = addr.rstrip(';').rstrip('.')
            urlList.append(addr)


            priceList.append(s_string[0].rstrip('.'))
        except AttributeError:
            continue
        except IndexError:
            continue


except HTTPError:
    print('error')


#showList 함수 정의
def showList():
    for i in range(0,10,1):
        print('[순위] : ',rankList[i],'\t[카페명] : ',nameList[i],'\t[메뉴명] : ',menuList[i],'\t[주소] : ',urlList[i],'[가격] : ',priceList[i])


showList()




#csv파일로 저장하기
data = {}
data['카페명'] = nameList
data['주소'] = urlList
data['가격'] = priceList

df = pd.DataFrame(data , index = rankList)
df.index.name = '순위'
df.to_csv("sandwiches.csv",mode="w",encoding='euc-kr')