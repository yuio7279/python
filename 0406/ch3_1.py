from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = bs4(html, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
    
title = getTitle('https://www.naver.com')
if title == None:
    print('x')
else:
    print(title.get_text())