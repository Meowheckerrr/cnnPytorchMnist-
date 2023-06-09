from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image


for i in range(0,100):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.ris.gov.tw/apply-idCard/app/idcard/IDCardReissue/main")
    ######
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(scroll_width, scroll_height)
    driver.save_screenshot('./cap_pic/fullpage.jpg')
    # 網頁中圖片驗證碼的位置
    element = driver.find_element_by_xpath('//*[@id="captchaImage_captcha-refresh"]')
    left = element.location['x']
    right = element.location['x'] + element.size['width']
    top = element.location['y']
    bottom = element.location['y'] + element.size['height']
    img = Image.open('./cap_pic/fullpage.jpg')
    img = img.crop((left, top, right, bottom))
    img = img.convert("RGB")
    img.save(f'./pic/{i}.jpg')
    print(f"已儲存:{i}.jpg")