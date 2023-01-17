from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C://Program Files (x86)/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
timeout = time.time() + 5
timeinterval = time.time() + 60 * 1

cookie = driver.find_element(By.ID, "cookie")

price_names = []
prices_nm = driver.find_elements(By.CSS_SELECTOR, "#store div b")
for values in prices_nm:
    if values.get_attribute("class") == "":
        pr_nm = values.text
        pr_nm = ''.join(filter(str.isalpha, pr_nm))
        price_names.append(pr_nm)
        price_names = [value for value in price_names if value]
print(f"Price Names: {price_names}")


def cookie_clicker():
    price_values = []
    prices = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for value in prices:
        if value.get_attribute("class") == "":
            price = value.text
            price = ''.join(filter(str.isdigit, price))
            price_values.append(int(price))
            price_values = [value for value in price_values if value]
    print(f"Price Values: {price_values}")

    expensive_item = len(price_values) - 1
    # money = int(driver.find_element(By.ID, "money").text)
    # print(f"money: {money}")
    try:
        click_item = driver.find_element(By.ID, f"buy{price_names[expensive_item]}")
        print(f"Click Item: {click_item.text}")
        click_item.click()
        print("Success")
    except IndexError:
        pass


Game_is_on = True
while Game_is_on:
    cookie.click()

    if time.time() > timeout:
        cookie_clicker()
        timeout = time.time() + 5
    if time.time() > timeinterval:
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(cookies_per_sec)
        break

driver.quit()
