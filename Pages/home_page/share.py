from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

class Share_post:
    def __init__(self, driver):
        self.driver = driver
        # used xpaths in project as unique IDs usually not available
        self.search_btn = "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[2]/a"
        self.search_bar = "/html/body/div[1]/section/nav[1]/div/header/div/h1/div/div/div/div[1]/label/input"
        self.user_btn = "/html/body/div[1]/section/main/div/div/ul/li[1]/a/div"
        self.post_btn = "eLAPa"
        self.more_btn = "/html/body/div[1]/section/main/div/div/article/div[1]/button"
        self.share_btn = "/html/body/div[4]/div/div/div/div/button[2]"
        self.share_direct_btn = "/html/body/div[4]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div"
        self.search_to_user = "/html/body/div[5]/div/div/div/div[1]/div/div[2]/input"
        self.to_user = "/html/body/div[5]/div/div/div/div[2]/div"
        self.send_btn = "/html/body/div[5]/div/div/header/div/div[2]/button"
        self.info_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.del_chat_btn = "/html/body/div[1]/section/div[2]/div/div[3]/div[1]/button"
        self.del_confirm = "/html/body/div[4]/div/div/div/div[2]/button[1]"

    def share_post(self):
        self.driver.find_element(By.XPATH, self.search_btn).click()
        self.driver.find_element(By.XPATH, self.search_bar).send_keys(self.get_from_users())
        self.driver.find_element(By.XPATH, self.user_btn).click()
        self.driver.find_element(By.CLASS_NAME, self.post_btn).click()
        self.driver.find_element(By.XPATH, self.more_btn).click()
        self.driver.find_element(By.XPATH, self.share_btn).click()
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.share_direct_btn))
                )
            element.click()
        except: 
            print("element not found")
        self.driver.find_element_by_xpath(self.search_to_user).send_keys(self.get_to_users())
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.to_user))
                )
            element.click()
        except: 
            print("element not found")
        # sleeps added for fun
        self.driver.find_element_by_xpath(self.send_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.info_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_chat_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_confirm).click()
        self.driver.get("https://www.instagram.com/")

    def get_from_users(self):
        from_users = ['user1','user2','user3']
        return random.choice(from_users)

    def get_to_users(self):
        to_users = ['user1','user2','user3']
        return random.choice(to_users)