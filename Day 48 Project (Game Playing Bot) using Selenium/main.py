from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

url = "http://orteil.dashnet.org/experiments/cookie/"
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.get(url=url)

# item_price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# item_price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
# print(f"The price is {item_price_whole}.{item_price_fraction}")

# event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
#
# # for events in event_names:
# #     print(events.text)
#
# for i in range(len(event_dates)):
#     events[i] = {
#         "time": event_dates[i].text,
#         "title": event_names[i].text
#     }
#
# print(events)
cookie = driver.find_element(by=By.ID, value="cookie")

menu = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
menu_items = [item.get_attribute("id") for item in menu]
# price = driver.find_element(by=By.CSS_SELECTOR, value="#store div b").text


time_start = time.time() + 5 * 60

while time.time() < time_start:
    start_time_in_loop = time.time()
    timeout = 5

    while time.time() - start_time_in_loop < timeout:
        cookie.click()
    money = int(driver.find_element(by=By.CSS_SELECTOR, value="#money").text.replace(",", ""))
    for item in list(reversed(menu_items)):
        try:
            item_price = driver.find_element(by=By.XPATH, value=f'//*[@id="{item}"]/b')
            if item_price.text != "":
                price = int(item_price.text.split("-")[1].strip(" ").replace(",", ""))
                if money >= price:
                    clicks = int(money/price)
                    for i in range(clicks):
                        try:
                            item_price.click()
                        except StaleElementReferenceException:
                            item_price = driver.find_element(by=By.XPATH, value=f'//*[@id="{item}"]/b')
                            item_price.click()
        except StaleElementReferenceException:
            break

cookies_per_minute = driver.find_element(by=By.CSS_SELECTOR, value="#cps").text
print(cookies_per_minute)





