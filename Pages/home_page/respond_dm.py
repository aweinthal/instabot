from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep

class Respond:
    def __init__(self, driver):
        self.driver = driver
        # used xpaths in project as unique IDs usually not available
        self.new_msg = "/html/body/div[1]/section/nav[1]/div/div/header/div/div[2]/a/div"
        self.popup_btn1 = "/html/body/div[5]/div/div/div/div[3]/button[2]"
        self.popup_btn2 = "/html/body/div[4]/div/div[2]/div/div[5]/button"
        self.msg_btn = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[1]/a/div/div[3]/div"
        self.msg_btn2 = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[2]/a/div/div[3]/div"
        self.msg_btn3 = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[3]/a/div/div[3]/div"
        self.msg_field = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea"
        self.msg_send_btn = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button"
        self.friend_reply = "/html/body/div[1]/section/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div"
        self.info_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.del_chat_btn = "/html/body/div[1]/section/div[2]/div/div[3]/div[1]/button"
        self.del_confirm = "/html/body/div[4]/div/div/div/div[2]/button[1]"


    def respond(self):
        self.driver.find_element_by_xpath(self.new_msg).click()
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup_btn1))
                )
            element.click()
        except:
            pass
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup_btn2))
                )
            element.click()
        except:
            pass
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.msg_btn))
                )
            element.click()
        except:
            pass
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.msg_btn2))
                )
            element.click()
        except:
            pass
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.msg_btn3))
                )
            element.click()
        except:
            pass
        # sleeps added for fun because process was happening too fast to watch:
        self.driver.find_element(By.XPATH, self.msg_field).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.msg_field).send_keys(self.get_response())
        sleep(1)
        self.driver.find_element(By.XPATH, self.msg_send_btn).click()
        sleep(1)
        # delete chat so xpath selects the right message next time:
        self.driver.find_element(By.XPATH, self.info_btn).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.del_chat_btn).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.del_confirm).click()
        sleep(1)
        self.driver.get("https://www.instagram.com/")

    def get_response(self):
        responses = ['quote1','quote2','quote3']
        question_responses = ['quote1','quote2','quote3']

        # checks if response is a question and responds accordingly
        element = self.driver.find_element_by_xpath(self.friend_reply).text
        if "?" in element:
            return random.choice(question_responses)
        else:
            return random.choice(responses)