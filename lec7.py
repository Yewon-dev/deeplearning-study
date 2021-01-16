import requests
from bs4 import BeautifulSoup

session = requests.session() # 세션 생성. 한번만 만들면 됨
# 로그인
url = "https://www.hanbit.co.kr/member/login_proc.php"
data = {
    "return_url" : "http://www.hanbit.co.kr/index.html",
    "m_id" : "<아이디>",
    "m_password" : "<비밀번호>"
}
response = session.post(url, data=data)
response.raise_for_status() # 요청이 실제로 이루어짐

# 원하는 정보 가져오기
url = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
response = session.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
text = soup.select_one(".mileage_section2 span").get_text()

print("이코인 : ", text)

# session.post(url)
# session.put(url)
# session.delete(url)