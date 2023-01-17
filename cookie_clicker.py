from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time

five_secs = time() + 5  # 5 seconds from now
five_min = time() + 60 * 5  # 5 minutes from now
chrome_driver_path = Service("C://Program Files (x86)/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
the_cookie = driver.find_element(By.ID, "cookie")


def buy_items():
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    available_items = []
    for i in items:
        if i.get_attribute("class") == "":
            available_items.append(i)
    expensive_item = len(available_items)-1
    try:
        available_items[expensive_item].click()
    except IndexError:
        pass


while True:
    the_cookie.click()
    if time() > five_secs:
        buy_items()
        five_secs = time() + 5
    if time() > five_min:
        cookies_per_sec = driver.find_element(By.ID, "cps")
        print(cookies_per_sec.text)
        break

driver.quit()