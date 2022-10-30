import numpy
import requests
from bs4 import BeautifulSoup

class Datas:
    stopword = []
    keyword = []
    
    def getUrl(self, url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        main = BeautifulSoup(r.text, 'html.parser')
        print(main.text)

data = Datas()
data.getUrl('https://www.ptt.cc/bbs/cookclub/M.1547728079.A.A7D.html')