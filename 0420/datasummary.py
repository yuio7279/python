from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

#문장 정제
def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence


#문장을 입력받아 가장 먼저 cleanInput에 입력
def cleanInput(content):
    content = content.upper()
    content = re.sub('\n',' ',content)
    content = bytes(content, 'utf-8')
    content = content.decode('ascii','ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

#정제된 문장을 n그램화한다.
def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

#
def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram
            in getNgramsFromSentence(sentence, n)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return(ngrams)

speech = 'http://pythonscraping.com/files/inaugurationSpeech.txt'
content = str(urlopen(speech).read(), 'utf-8')
ngrams = getNgrams(content, 2)
print(ngrams)
