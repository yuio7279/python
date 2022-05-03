from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
info_list = []

def getPageLinks():         #영화 링크 가져오기
        links = []
    
        url = "https://movie.naver.com/movie/running/current.naver"
        req = requests.get(url, headers=headers)
        soup = BS(req.text, 'lxml')
        movielinks = soup.select('dl.lst_dsc dt.tit a[href]')

        for movielink in movielinks:           
            link = str(movielink.get('href'))
            links.append("https://movie.naver.com"+link)
        return links        



def getData(links:list):
    for link in links[:5]: #영화5개
        req = requests.get(link, headers=headers)
        soup = BS(req.text, 'lxml')
        info = soup.find('div', class_='mv_info')


        titles = info.select('h3.h_movie a')[0].text

        rates = info.select('span.st_off span.st_on')[0].text

        genres = soup.select('dl.info_spec dd p span')[0]   
        genres = genres.findAll('a')
        genres = getList(genres)

        dates = soup.select('dl.info_spec dd p span')[3]
        dates = getList(dates)
        dates = dates[1]+dates[4]
        
        summary = soup.select('div.story_area p.con_tx')
        summary = getList(summary)
        
        info_dict = {
            'title': titles,
            'rate' : rates,
            'genre': genres,
            'date' : dates,
            'summary' : summary
        }
        info_list.append(info_dict)
    return info_list
        
def getList(genres):    #데이터가공
    genList = []
    for genre in genres:
        genre = genre.text.replace(u'\r\xa0', u' ')
        genre = genre.replace(u'\xa0', u' ')
        genList.append(genre)

    return genList


def showList():
    info_list = getData(getPageLinks())
    for info_dict in info_list:
        print('제목 :',info_dict['title'],'\t평점 :',info_dict['rate'],'\n장르 :',info_dict['genre'],'\t개봉일 :',info_dict['date'],'\n줄거리 :',info_dict['summary'],'\n\n')
        
showList()