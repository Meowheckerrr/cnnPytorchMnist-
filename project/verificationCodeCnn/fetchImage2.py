from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--headless") # 選擇開啟瀏覽器的模式，這裡是無頭模式
driver = webdriver.Chrome(options=chrome_options) # 開啟瀏覽器

url = "https://www.example.com" # 要爬取的網站
driver.get(url) # 前往網站

# 網頁中圖片驗證碼的位置
#element = driver.find_element_by_xpath('//*[@id="captchaImage_captcha-refresh"]')
time.sleep(0)
element = driver.find_element(By.XPATH, '//*[@id="captchaImage_captcha-refresh"]')
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']

# 截圖並存檔
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width, scroll_height)
driver.save_screenshot('./cap_pic/fullpage.jpg')

img = Image.open('./cap_pic/fullpage.jpg')
img = img.crop((left, top, right, bottom))
img = img.convert("RGB")
img.save('captcha.jpg')

driver.quit() # 關閉瀏覽器