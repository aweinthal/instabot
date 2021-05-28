from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Like_Pics:
    def __init__(self,driver):
        self.driver = driver

    def like_pics(self):
        for btn in self.driver.find_elements_by_class_name("ZyFrc"):
            try:
                btn.click()
                btn.click()
                sleep(0.5)
            except:
                pass