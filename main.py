from encodings import utf_8
import re
import numpy
import requests

class Datas:
    
    stopword = []
    keyword = []

    def getUrl(url, method="get"):
        r = requests
        if method == "get":
            r.get(url)
        elif method == "post":
            r.post(url)
        r.encoding = 'utf-8'
        print(r.text)

data = Datas()
#data.getUrl('https://www.ptt.cc/bbs/cookclub/M.1547728079.A.A7D.html')

r = requests.get('https://www.ptt.cc/bbs/cookclub/M.1547728079.A.A7D.html')
r.encoding = 'utf-8'
print(r)