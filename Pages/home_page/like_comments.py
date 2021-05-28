from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Like_Comments:
    def __init__(self, driver):
        self.driver = driver
        self.first_pic = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[2]"
        self.comments_btn = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[3]/div[1]/div/div[2]/div[1]"
        self.popup = "/html/body/div[4]/div/div/div/div[3]/button[2]"

    def like_comments(self):

        # scroll to first post to make comments btn selectable:
        scroll_to = self.driver.find_element_by_xpath(self.first_pic)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.comments_btn))
                )
            element.click()
        except: 
            print("element not found")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup))
                )
            element.click()
        except: 
            pass
        # likes all comments on most recent post:
        like_btns = self.driver.find_element(By.CLASS_NAME, "_8-yf5 ")
        for like in like_btns:
            try:
                like.click()
            except:
                pass
        self.driver.get("https://www.instagram.com/")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup))
                )
            element.click()
        except:
            pass