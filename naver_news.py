import urllib.request
from bs4 import BeautifulSoup
import time
import ssl

context = ssl._create_unverified_context()


# 기사 목록 가져오기
url ="https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"
response = urllib.request.urlopen(url,context=context)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#main_content a")
# 기사 가져오기
for result in results:
    # 기사 제목
    print("제목: ", result.attrs["title"])
    
    # 기사 내용
    url_article = result.attrs["href"] 
    response = urllib.request.urlopen(url_article,context=context)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.select_one("#articleBodyContents")
    print(content.contents) # string으로만 하면 텍스트만 들고옴. contents라고 해야 태그 안에 있는 문자열도 들고옴

    # 5초 휴식
    time.sleep(5)

    print(" ")