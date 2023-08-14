# # selenium 설치 후 import
# from selenium import webdriver
# # Chrome을 조작용 driver로 선언
# driver = webdriver.Chrome('C:/Users/Soyee/Downloads/chromedriver.exe')
# # 크롬드라이버로 웹 사이트 접속
# driver.get('https://www.naver.com/')

import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_options = Options()

# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)

# USB error 해결
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)


# USB error 해결
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)


# 웹페이지 해당 주소 이동
driver.get("https://ceo.baemin.com/")


