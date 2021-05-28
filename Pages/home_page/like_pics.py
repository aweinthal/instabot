from selenium.webdriver.common.by import By

class Like_Pics:
    def __init__(self,driver):
        self.driver = driver

    def like_pics(self):
        for btn in self.driver.find_element(By.CLASS_NAME, "ZyFrc"):
            try:
                btn.click()
                btn.click()
            except:
                pass