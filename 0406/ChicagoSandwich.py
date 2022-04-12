from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen , Request
import pandas as pd

menuList = []
nameList = []
rankList = []
priceList = []
urlList = []
s_urlList = []          


try:
    urlTicker = Request('https://www.chicagomag.com/chicago-magazine/november-2020/sandwich-city/the-10-best-sandwiches/', headers={'User-Agent':'Mozilla/5.0'})
    readTicker = urlopen(urlTicker)
    soup = bs(readTicker, 'html.parser')
    
    for figcaption in soup.findAll('figcaption'):               
        try:
            menuList.append(figcaption.find('strong').getText())   #메뉴 가져오는 부분입니다

            h2 = figcaption.findAll('h2')                        
            rankList.append(h2[0].getText())                 #랭킹 가져오는 부분입니다
            nameList.append(h2[1].getText())                 #매장명 가져오는 부분입니다.

        except AttributeError:                          #figcaption의 첫번째 리턴값의 strong, h2태그가 없는것을 처리
            continue                                         



    for em in soup.findAll('em'):
        try:
            s_string = em.getText().split()
            addr = s_string[1]+' '+s_string[2]+' '+s_string[3]+' '+s_string[4]      #주소 구하는 부분입니다

            urlList.append(addr.rstrip(';').rstrip('.'))
            priceList.append(s_string[0].rstrip('.'))   


            if len(s_string) > 5:                                                 #주소가 2개인 매장 분류입니다
                second_addr = s_string[5]+' '+s_string[6]+' '+s_string[7]+' '+s_string[8]
                s_urlList.append(second_addr.rstrip(';').rstrip('.'))
            else:
                s_urlList.append(None)                                              #주소가 1개면 주소2리스트에 None 추가

        
        except IndexError:                                              #s_string[4]까지 담기지 않는 경우
            continue


except HTTPError:
    print('HTTPError')


#showList 함수 정의
def showList():
    for i in range(0,10,1):
        print('[순위] : ',rankList[i],' [카페명] : ',nameList[i],'[메뉴명] : ',menuList[i],'[가격] : ',priceList[i],'[주소] : ',urlList[i],'[주소2] : ',s_urlList[i])


showList()




#csv파일로 저장하기
data = {}
data['카페명'] = nameList
data['주소'] = urlList
data['주소2'] = s_urlList
data['메뉴명'] = menuList
data['가격'] = priceList
                                                        #encoding='euc-kr' > \xe9 error > utf-8 > 한글깨짐 > utf-8-sig
                                                        #\xe9 : 악센트 부호가 붙은 문자열  
df = pd.DataFrame(data , index = rankList)
df.index.name = '순위'                                      
df.to_csv("sandwiches.csv",mode="w",encoding='utf-8-sig')       
