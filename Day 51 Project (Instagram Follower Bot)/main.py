import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


USERNAME = "IG USERNAME"
PASSWORD = "IG PASSWORD"

CHROME_DRIVER_PATH = "CHROME DRIVER PATH"
service = Service(CHROME_DRIVER_PATH)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=option)

class InstaFollower:
    def __init__(self):
        self.driver = driver

    def login(self):
        login_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url=login_url)
        time.sleep(3)
        username = self.driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[1]/div/label/input")
        username.send_keys(USERNAME)
        time.sleep(1)
        password = self.driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[2]/div/label/input")
        password.send_keys(PASSWORD)
        time.sleep(1)
        login_button = self.driver.find_element(by=By.XPATH, value="//*[@id='loginForm']/div/div[3]/button")
        login_button.click()
        time.sleep(5)
        not_now_save_button = self.driver.find_element(by=By.XPATH, value="//*[@id='mount_0_0_8B']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
        not_now_save_button.click()
        time.sleep(2)
        not_now_notif_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        not_now_notif_button.click()
        time.sleep(1)




    def find_followers(self):
        pass

    def follow(self):
        pass



ig = InstaFollower()
ig.login()