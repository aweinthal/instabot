from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Functions.matt_quotes import rand_quote

class Comment:
    def __init__(self,driver):
        self.driver = driver
        # used xpaths in project as unique IDs usually not available
        self.first_pic = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[2]"
        self.comment_btn = "/html/body/div[1]/section/main/section/div[3]/div[1]/div/article[1]/div[3]/section[1]/span[2]"
        self.comment_box = "/html/body/div[1]/section/main/section/div/form/textarea"
        self.post_btn = "/html/body/div[1]/section/main/section/div/form/button"
        self.popup_btn = "/html/body/div[1]/section/div[2]/div/div[1]/button/span"
        self.popup_btn2 = "/html/body/div[4]/div/div/div/div[3]/button[2]"
        self.use_app_popup = "/html/body/div[1]/section/div[2]/div/div[1]/button"

    def comment(self):

        try:
            self.driver.find_element(By.XPATH, self.use_app_popup).click()
        except:
            pass
        # scroll to first post to make comment btn selectable:
        scroll_to = self.driver.find_element_by_xpath(self.first_pic)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup_btn))
                )
            element.click()
        except:
            pass
        self.driver.find_element(By.XPATH, self.comment_btn).click()
        # selects and enters random quote as comment:
        self.driver.find_element(By.XPATH, self.comment_box).send_keys(rand_quote("comment"))
        self.driver.find_element(By.XPATH, self.post_btn).click()
        self.driver.get("https://www.instagram.com/")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup_btn2))
                )
            element.click()
        except:
            pass