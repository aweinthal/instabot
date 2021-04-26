import autoit
from matt_quotes import rand_quote
from time import sleep
import random

class Post:
    def __init__(self, driver):
        self.driver = driver
        self.post_button = "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]"
        self.next_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.desc_box = "/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea"
        self.share_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"

    # pics in local dir named with a number only
    def rand_pic(self):
        return str(random.choice(range(1,11)))

    def post(self):
        self.driver.find_element_by_xpath(self.post_button).click()
        sleep(3)
        # autoit for uploading pics from local dir
        handle = "[CLASS:#32770; TITLE:Open]"
        autoit.win_wait(handle, 3)
        autoit.control_set_text(handle, "Edit1", fr"C:\Users\Alex\Desktop\mattbotpics\{self.rand_pic()}.jpg")
        autoit.control_click(handle, "Button1")
        self.driver.find_element_by_xpath(self.next_btn).click()
        self.driver.find_element_by_xpath(self.desc_box).send_keys(rand_quote("post"))
        self.driver.find_element_by_xpath(self.share_btn).click()
        # sleep to allow time to upload post
        sleep(15)