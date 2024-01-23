from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "http://secure-retreat-92358.herokuapp.com/"
firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)

driver.get(url=url)

# article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a").text
# print(article_count)

# search_bar = driver.find_element(by=By.NAME, value="search")
# search_bar.send_keys("Wow")
# search_bar.send_keys(Keys.ENTER)

first_name = driver.find_element(by=By.NAME, value="fName")
last_name = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
signup_button = driver.find_element(by=By.CLASS_NAME, value="btn")

first_name.send_keys("Tracy")
last_name.send_keys("McGravy")
email.send_keys("tmacgravy21@gmail.com")
signup_button.click()
