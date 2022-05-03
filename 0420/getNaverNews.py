from bs4 import BeautifulSoup
import requests
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}



def get_soup_obj(news_link):
    res = requests.get(news_link, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

default_img = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#'
for sid in ['100']:#, '101', '102']:
    #sec_url_n = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
    sec_url = 'https://news.naver.com/main/list.nhn?mpde=LSD&mid=sec'+'&sid1='+sid
    print('section url : ', sec_url)

    #해당분야 상위 뉴스 html 가져오기
    soup = get_soup_obj(sec_url)

    #상위 3개뉴스 가져오기 파싱
    lis3 = soup.find('ul', class_='type06_headline').find_all('li',limit=3)


