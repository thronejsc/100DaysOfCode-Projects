import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import requests


FORMS_URL = "YOUR GOOGLE FORMS URL"
SHEETS_URL = "YOUR GOOGLE SHEET URL"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=ZILLOW_CLONE_URL)
webpage_html = response.text
soup = BeautifulSoup(webpage_html, "html.parser")

addresses = []
links = []

properties = soup.findAll(name="a", class_="StyledPropertyCardDataArea-anchor")
property_prices = soup.findAll(name="span", class_="PropertyCardWrapper__StyledPriceLine")

for i in properties:
    address = i.find(name="address").getText().strip()
    addresses.append(address)
    link = i['href']
    links.append(link)

prices = [price.getText().strip("+/mo").strip("+ 1 bd") for price in property_prices]


CHROME_DRIVER_PATH = "CHROME_DRIVER_PATH"
service = Service(CHROME_DRIVER_PATH)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=option)

open_forms = driver.get(url=FORMS_URL)
time.sleep(3)

for i in range(len(addresses) + 1):

    input_address = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_address.send_keys(addresses[i])
    time.sleep(1)

    input_price = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_price.send_keys(prices[i])
    time.sleep(1)

    input_link = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    input_link.send_keys(links[i])
    time.sleep(1)

    submit_button = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
    submit_button.click()
    time.sleep(1)

    submit_again = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submit_again.click()
    time.sleep(1)








