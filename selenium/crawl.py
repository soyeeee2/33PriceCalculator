import selenium
import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By


chrome_options = Options()

# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)

# USB error 해결
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)



#윈도우 위치, 사이즈 조정
driver.set_window_position(0,0) 
driver.set_window_size(1920, 1080) 

# 웹페이지 해당 주소 이동
driver.get("https://ceo.baemin.com/")
time.sleep(2)

#main to login_page
go_to_login = driver.find_element(By.CLASS_NAME, "Button__StyledButton-sc-394bsp-0-Component")
go_to_login.click()

#login
id_input = driver.find_element(By.NAME, "id")
pwd_input = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CLASS_NAME, "Button__StyledButton-sc-1cxc4dz-0")

id_input.send_keys('33soyee')
pwd_input.send_keys('sp090504!!')
login_btn.click()

#go to menus
# driver.find_element(By.LINK_TEXT, '배민셀프서비스').click()
# driver.find_element(By.CLASS_NAME, 'MenuItem-module__yFCx').click()