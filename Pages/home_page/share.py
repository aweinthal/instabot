from time import sleep
import random

class Share_post:
    def __init__(self, driver):
        self.driver = driver

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
        self.driver.find_element_by_xpath(self.search_btn).click()
        self.driver.find_element_by_xpath(self.search_bar).send_keys(self.get_from_users())
        self.driver.find_element_by_xpath(self.user_btn).click()
        self.driver.find_element_by_class_name(self.post_btn).click()
        self.driver.find_element_by_xpath(self.more_btn).click()
        self.driver.find_element_by_xpath(self.share_btn).click()
        sleep(2)
        self.driver.find_element_by_xpath(self.share_direct_btn).click()
        self.driver.find_element_by_xpath(self.search_to_user).send_keys(self.get_to_users())
        sleep(2)
        self.driver.find_element_by_xpath(self.to_user).click()
        self.driver.find_element_by_xpath(self.send_btn).click()
        self.driver.find_element_by_xpath(self.info_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_chat_btn).click()
        sleep(1)
        self.driver.find_element_by_xpath(self.del_confirm).click()
        sleep(1)
        self.driver.get("https://www.instagram.com/")

    def get_from_users(self):
        from_users = ['user1','user2','user3']
        return random.choice(from_users)

    def get_to_users(self):
        to_users = ['user1','user2','user3']
        return random.choice(to_users)