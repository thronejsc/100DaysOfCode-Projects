import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


USERNAME = "tmacgravy21"
PASSWORD = "natehiggersgoogleceo"

CHROME_DRIVER_PATH = "C:/Users/ejcan/Desktop/chromedriver-win64/chromedriver.exe"
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
        time.sleep(7)
        not_now_save_button = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        not_now_save_button.click()
        time.sleep(2)
        not_now_notif_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        not_now_notif_button.click()
        time.sleep(2)

    def find_followers(self):
        target_url = "https://www.instagram.com/spiderman/"
        self.driver.get(url=target_url)
        time.sleep(5)
        followers = self.driver.find_element(by=By.XPATH, value="//a[contains(text(), ' followers')]")
        followers.click()
        time.sleep(5)
        pop_up_followers = self.driver.find_element(by=By.XPATH,
                                                    value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_followers)

    def follow(self):
        follow = self.driver.find_elements(by=By.CSS_SELECTOR, value="._aano button")
        try:
            for i in follow:
                i.click()
                time.sleep(1)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
            cancel_button.click()


ig = InstaFollower()
ig.login()
ig.find_followers()
ig.follow()
