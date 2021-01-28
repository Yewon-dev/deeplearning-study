### 여는 태그와 닫는 태그
# 1. <태그></태그> ## 요소 element
# 2. <태그 />
# 
### 콘텐츠
# <태그>{{콘텐츠}}</태그>
# <태그>
#   <태그></태그>
#   <태그></태그>
# </태그>
# 
### 속성
# <태그 속성="값" 속성="값">{{콘텐츠}}</태그>

# xml 파싱

from bs4 import BeautifulSoup
import urllib.request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()

soup = BeautifulSoup(xml, "html.parser")
seoul = soup.find_all("location")[0]
datas = seoul.find_all("data")

for item in datas:
    print(item.find("wf").text)

