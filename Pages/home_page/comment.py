from matt_quotes import rand_quote
from time import sleep


class Comment:
    def __init__(self,driver):
        self.driver = driver
        self.first_pic = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[2]"
        self.comment_btn = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[3]/section[1]/span[2]"
        self.comment_box = "/html/body/div[1]/section/main/section/div/form/textarea"
        self.post_btn = "/html/body/div[1]/section/main/section/div/form/button"
        self.popup_btn = "/html/body/div[1]/section/div[2]/div/div[1]/button/span"
        self.popup_btn2 = "/html/body/div[4]/div/div/div/div[3]/button[2]"
        self.use_app_banner = "/html/body/div[1]/section/div[2]/div/div[1]/button"

    def comment(self):
        try:
            self.driver.find_element_by_xpath(self.use_app_banner).click()
        except:
            pass
        scroll_to = self.driver.find_element_by_xpath(self.first_pic)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
        sleep(2)
        try:
            self.driver.find_element_by_xpath(self.popup_btn).click()
        except:
            pass
        self.driver.find_element_by_xpath(self.comment_btn).click()
        self.driver.find_element_by_xpath(self.comment_box).send_keys(rand_quote("comment"))
        self.driver.find_element_by_xpath(self.post_btn).click()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        try:
            self.driver.find_element_by_xpath(self.popup_btn2).click()
        except:
            pass