from time import sleep

class Like_Comments:
    def __init__(self, driver):
        self.driver = driver
        self.first_pic = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[2]"
        self.comments_btn = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[3]/div[1]/div/div[2]/div[1]"
        self.popup = "/html/body/div[4]/div/div/div/div[3]/button[2]"

    def like_comments(self):

        scroll_to = self.driver.find_element_by_xpath(self.first_pic)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
        sleep(2)
        self.driver.find_element_by_xpath(self.comments_btn).click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(self.popup).click()
        except:
            pass
        like_btns = self.driver.find_elements_by_class_name("_8-yf5 ")
        for like in like_btns:
            try:
                like.click()
            except:
                pass
        self.driver.get("https://www.instagram.com/")
        try:
            self.driver.find_element_by_xpath(self.popup).click()
        except:
            pass