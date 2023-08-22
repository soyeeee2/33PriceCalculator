import selenium
import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import pyperclip

chrome_options = Options()

# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)

# USB error 해결
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 사용자 설정
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
chrome_options.add_argument("app-version=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

#윈도우 위치, 사이즈 조정
driver.set_window_position(0,0) 
driver.set_window_size(1920, 1080) 

# 웹페이지 해당 주소 이동
driver.get("https://biz-member.baemin.com/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2F")


time.sleep(2)




#login
id_input = driver.find_element(By.NAME, "id")
pwd_input = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CLASS_NAME, "Button__StyledButton-sc-1cxc4dz-0")

uid = '33soyee'
upw = 'sp090504!!'


# id 입력
# 입력폼 클릭 -> paperclip에 선언한 uid 내용 복사 -> 붙여넣기
id_input.click()
pyperclip.copy(uid)
id_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
# 입력폼 클릭 -> paperclip에 선언한 upw 내용 복사 -> 붙여넣기
pwd_input.click()
pyperclip.copy(upw)
pwd_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#로그인 버튼 클릭
login_btn.click()
time.sleep(2)

# 현재 창 핸들 저장
main_window_handle = driver.current_window_handle

##배민셀프서비스 찾을때까지 wait
wait = WebDriverWait(driver, 10)

self_service = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "배민셀프서비스")))

if self_service:
    desired_element = self_service[0]
    desired_element.click()
else:
    print("Element not found")

time.sleep(2)

all_window_handles = driver.window_handles

# 새로 열린 탭을 찾기 위해 핸들 비교
main_handle = driver.current_window_handle

new_window_handle = None
for handle in all_window_handles:
    if handle != main_window_handle:
        new_window_handle = handle
        break
    
# 새로 열린 탭으로 전환
if new_window_handle:
    driver.switch_to.window(new_window_handle)
else:
    print("New window handle not found.")



# 새 탭에서 작업 수행 (예: 새로 열린 탭의 제목 가져오기)
# new_window_title = driver.title
# print("New tab title:", new_window_title)


time.sleep(5)


go_to_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "가게 메뉴판 편집")))
go_to_menu.click()


#메뉴판 접근
depth_ul = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'menuGroup-module__m_jN')))


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

menupan = soup.select_one('#root > div > div.frame-container > div.frame-wrap > div.frame-body > div > ul')

menuItems = menupan.find_all("li", "menuGroup-module__m_jN")

def mnet_Crawling():
    menu_list = []
    
    # 개별 category
    for item in menuItems:
        categoryTitle = item.find('span', "bsds-typography-text20").get_text()

 
        
        
        depth_li = item.find_all('li', "menuItem-module__rdCR")
        menuInfo = []
        
       
        # 개별 menu
        for menu in depth_li:
            #메뉴 이름
            menuTitle = menu.find('span', 'menuInfo-module__p2u1').get_text()
            
            
            #메뉴 구성
            menuTexts = menu.find('div', 'menuInfo-module__tSV5')
            
            child_count = len(menuTexts.contents)
            if child_count > 2:
                menuDetails_span = menu.find('span', class_=['menuInfo-module__YrUk', 'css-9h5tob']).get_text()
                menuDetails = menuDetails_span.replace(' ', '').split('+')
            else:
                menuDetails = ''
                
            
            #메뉴 가격
            price_spans = menu.find_all('span', class_=['bsds-typography-text14', 'css-2bmumi'])  
            if price_spans:  # price_spans가 비어있지 않은 경우에만 실행
                # 가격 정보의 마지막 요소 선택
                last_price = price_spans[-1].get_text()
                # 가격 문자열에서 '원'과 쉼표를 제거한 후 정수로 변환
                price = int(last_price.replace('원', '').replace(',', ''))
            else:
                "can't find price"
                
                
            # img = menu.find('img', 'bsds-thumbnail-image')['src']
            # img = menu.find('img').get('src')
            imgSrc = [img['src'] for img in menu.find_all('img')]
                
            menuInfo.append({"menuTitle": menuTitle, "menuDetails": menuDetails, "price": price})
        
        
        menu_list.append({"categoryTitle": categoryTitle, "menuInfo": menuInfo, "imgSrc": imgSrc})


    return menu_list

result = mnet_Crawling()
print(result)


driver.quit()