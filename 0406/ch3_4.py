
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
import re

pages = set()


def getLinks(pageUrl):
    html = urlopen(pageUrl)
    bs = bs4(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').findAll('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError as e:
        print('This page is missing something! No worries though!')
        
    for link in bs.findAll('a' , re.compile('^(/wiki/)')):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            pages.add(newPage)
            print('새로운 페이지 발견')
            getLinks(newPage)
        else:
            print('s')
getLinks('http://en.wikipedia.org')

