from selenium import webdriver


url = "https://nid.naver.com/nidlogin.login"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(chrome_options=options,executable_path="./chromedriver")
# 3초 대기하기
browser.implicitly_wait(3)
# URL 읽어 들이기
browser.get(url)

# 로그인
element_id = browser.find_element_by_id("id") # 아이디 텍스트 입력 상자
element_id.clear()
element_id.send_keys("")

element_pw = browser.find_element_by_id("pw") # 비밀번호 텍스트 입력 상자
element_pw.clear()
element_pw.send_keys("")

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()

# 메일 페이지 열기
browser.get("https://mail.naver.com")

# 화면을 캡쳐해서 저장하기
browser.save_screenshot("Website_D.png")

# 메일제목 가져오기
titles = browser.find_element_by_css_selector("strong.mail_title")
for title in titles:
    print("-", title.text)

# 브라우저 종료하기
browser.quit()