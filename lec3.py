#
#
# 방식 : GET
# 대상 : https://search.naver.com => 호스트 이름
# 추가적인 정보
# - 경로: /search.naver
# - 데이터: ?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B3%A0%EC%96%91%EC%9D%B4

import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = { 
    "where" : "nexearch",
    "sm" : "top_hty",
    "fbm" : 0,
    "ie" : "utf8",
    "query" : "고양이"
}
params = urllib.parse.urlencode(values)


url = api + "?" + params
#print(url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8") # euc-kr
print(text)