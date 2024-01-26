import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


TWITTER_USERNAME = "TWITTER_USERNAME"
TWITTER_PASSWORD = "TWITTER_PASSWORD"

CHROME_DRIVER_PATH = "CHROME_DRIVER_PATH"
service = Service(CHROME_DRIVER_PATH)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=option)

SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/home"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEEDTEST_URL)
        go_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        go_button.click()
        time.sleep(70)
        self.down = float(self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text)
        self.up = float(self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)
        print(f"DOWN: {self.down}")
        print(f"UP: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        time.sleep(5)
        username = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_USERNAME)
        time.sleep(2)
        next_button = self.driver.find_element(by=By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()
        time.sleep(5)
        password = self.driver.find_element(by=By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        login_button = self.driver.find_element(by=By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        login_button.click()
        time.sleep(15)
        tweet_button = self.driver.find_element(by=By.XPATH, value="//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        tweet_button.click()
        time.sleep(5)
        #draft = self.driver.find_element(by=By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span")
        draft = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        draft.send_keys(f"My current internet speed is {self.down}Mbps Download and {self.up}Mbps Upload")

        time.sleep(3)
        post_button = self.driver.find_element(by=By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]")
        post_button.click()
        print("Tweet has been successfully made")


bot = InternetSpeedTwitterBot()
bot.tweet_at_provider()
