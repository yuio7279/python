
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen(pageUrl)
    bss = bs(html,'html.parser')
    for link in bss.findAll('a' , href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs not in pages:
                newPage = link.attrs['href']
                pages.add[newPage]
                getLinks(newPage)
                print(newPage)
getLinks('http://naver.com')
