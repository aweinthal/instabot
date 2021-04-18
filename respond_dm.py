import random
from time import sleep

class Respond:
    def __init__(self, driver):
        self.driver = driver
        
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
        sleep(2)
        try:
            self.driver.find_element_by_xpath(self.popup_btn1).click()
            sleep(1)
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.popup_btn2).click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.msg_btn).click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.msg_btn2).click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.msg_btn3).click()
        except:
            pass
        # sleeps added for fun because process was happening too fast to watch:
        self.driver.find_element_by_xpath(self.msg_field).click()
        sleep(2)
        self.driver.find_element_by_xpath(self.msg_field).send_keys(self.get_response())
        sleep(1)
        self.driver.find_element_by_xpath(self.msg_send_btn).click()
        sleep(1)
        # delete chat so xpath selects the right message next time:
        self.driver.find_element_by_xpath(self.info_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_chat_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_confirm).click()
        sleep(1)
        self.driver.get("https://www.instagram.com/")

    def get_response(self):
        responses = ['quote1','quote2','quote3']
        question_responses = ['quote1','quote2','quote3']

        element = self.driver.find_element_by_xpath(self.friend_reply).text
        if "?" in element:
            return random.choice(question_responses)
        else:
            return random.choice(responses)