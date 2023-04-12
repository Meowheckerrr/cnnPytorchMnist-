

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time

# 初始化 Selenium
selenium_service = Service('./chromedriver.exe')
selenium_service.start()
chrome_options = Options()
chrome_options.add_argument('--headless')  # 設定為無頭模式
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

num_images = 500

for i in range(num_images):

    # 進入目標網站
    driver.get('https://www.ris.gov.tw/apply-idCard/app/idcard/IDCardReissue/main')

    # 等待一段時間，讓圖片載入完畢 其實不用等
    #time.sleep(1)

    # 取得圖片元素
    element = driver.find_element(By.ID, 'captchaImage_captcha-refresh')

    # 取得圖片網址
    image_url = element.get_attribute('src')
    fullImage='https://www.ris.gov.tw' + image_url
    print(fullImage)

    response = requests.get(image_url)

    with open("trainingData/{}.jpg".format(i), "wb") as f:
        f.write(response.content)


# 關閉瀏覽器
driver.quit()