from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Watch_Stories:
    def __init__(self, driver):
        self.driver = driver
        self.stories_btn = "/html/body/div[1]/section/main/section/div[1]/div/div/div/div[2]/button"
        self.popup = "/html/body/div[4]/div/div/div/div[3]/button[2]"

    def watch_stories(self):
        self.driver.find_element(By.XPATH, self.stories_btn).click()
        # watch for 40 secs then exit:
        sleep(40)
        self.driver.get("https://www.instagram.com/")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup))
                )
            element.click()
        except: 
            pass