import requests
from urllib.parse import quote

def get1000Result (keyword):
    list = []
    for num in range(0, 10):
        list = list + call(keyword, num * 100 + 1)['items']
    return list
    
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)
    result = requests.get(url = url, headers={"X-Naver-Client-Id": "SD0DKeX9rskF9DIy4heT", 
                                   "X-Naver-Client-Secret": "JrIO2TLrA5"
                          })
    print(result)
    return result.json()
