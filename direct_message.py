from time import sleep
from matt_quotes import rand_quote
import random

class Direct_Message:
    def __init__(self, driver):
        self.driver = driver
        
        self.messages_btn = "/html/body/div[1]/section/nav[1]/div/div/header/div/div[2]/a"
        self.new_msg_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.search_users = "/html/body/div[1]/section/div[2]/div/div[1]/div/div[2]/input"
        self.click_user = "/html/body/div[1]/section/div[2]/div/div[2]/div"
        self.next_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button/div"
        self.message_field = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea"
        self.message_send_btn = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button"
        self.popup1 = "/html/body/div[5]/div/div/div/div[3]/button[2]"
        self.popup2 = "/html/body"
        self.info_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.del_chat_btn = "/html/body/div[1]/section/div[2]/div/div[3]/div[1]/button"
        self.del_confirm = "/html/body/div[4]/div/div/div/div[2]/button[1]"

    def direct_message(self):

        self.driver.find_element_by_xpath(self.messages_btn).click()
        sleep(1)
        try:
            self.driver.find_element_by_xpath(self.popup1).click()
            sleep(1)
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.popup2).click()
        except:
            pass
        self.driver.find_element_by_xpath(self.new_msg_btn).click()
        self.driver.find_element_by_xpath(self.search_users).click()
        self.driver.find_element_by_xpath(self.search_users).send_keys(self.get_to_users())
        sleep(2)
        self.driver.find_element_by_xpath(self.click_user).click()
        self.driver.find_element_by_xpath(self.next_btn).click()
        self.driver.find_element_by_xpath(self.message_field).send_keys(rand_quote("dm"))
        self.driver.find_element_by_xpath(self.message_send_btn).click()
        self.driver.find_element_by_xpath(self.info_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_chat_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_confirm).click()
        sleep(1)
        self.driver.get("https://www.instagram.com/")
        

    def get_to_users(self):
        to_users = ['user1','user2']
        return random.choice(to_users)