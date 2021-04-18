
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.email_box = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input"
        self.pw_box = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
        self.login_btn1 = "/html/body/div[1]/section/main/article/div/div/div/div[2]/button"
        self.login_btn2 = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button"
        self.popup_btn1 = "/html/body/div[4]/div/div/div/div[3]/button[2]"
        self.popup_btn2 = "/html/body/div[1]/section/main/div/div/div/button"

    def login(self, username, pw):
        self.driver.find_element_by_xpath(self.login_btn1).click()
        self.driver.find_element_by_xpath(self.email_box).send_keys(username)
        self.driver.find_element_by_xpath(self.pw_box).send_keys(pw)
        self.driver.find_element_by_xpath(self.login_btn2).click()
        try:
            self.driver.find_element_by_xpath(self.popup_btn1).click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.popup_btn2).click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(self.popup_btn1).click()
        except:
            pass