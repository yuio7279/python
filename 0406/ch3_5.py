
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
import re
import datetime
import random

html = urlopen('https://pelicana.co.kr/store/stroe_search.html')
bs = bs4(html, 'html.parser')

for link in bs.findAll('tbody'):
    print(link)