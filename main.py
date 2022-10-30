import requests
from bs4 import BeautifulSoup

class Datas:
    stopword = []
    keyword = []
    urlList = [
        'https://www.ptt.cc/bbs/cookclub/M.1547728079.A.A7D.html',
        'https://ptthito.com/cookclub/m-1376469852-a-91f/',
        'https://www.dcard.tw/f/cooking/p/236411834',
        'https://www.dcard.tw/f/food/p/239812341'
        ]

    def getUrl(url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        main = BeautifulSoup(r.text, 'html.parser')
        print("Now showing", url)
        print(main.text)

    for url in urlList:
        getUrl(url)

data = Datas()