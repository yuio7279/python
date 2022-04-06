
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs1 = bs(html,'html.parser')
for link in bs1.find('div' , {'id' : 'bodyContent' }).findAll('a',href = re.compile('^(/wiki/)((?!:(.(*S')):
    if 'href' in link.attrs:
        print(link.attrs['href'])