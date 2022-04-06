from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# nameList = bs.findAll('span')
# for name in nameList:
#     print(name)

# print(bs.span.h1)


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id': 'giftList'}).children:
    print(child)