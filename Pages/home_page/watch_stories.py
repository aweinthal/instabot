from time import sleep

class Watch_Stories:
    def __init__(self, driver):
        self.driver = driver
        self.stories_btn = "/html/body/div[1]/section/main/section/div[1]/div/div/div/div[2]/button"
        self.popup = "/html/body/div[4]/div/div/div/div[3]/button[2]"

    def watch_stories(self):
        self.driver.find_element_by_xpath(self.stories_btn).click()
        # watch for 40 secs then exit:
        sleep(40)
        self.driver.get("https://www.instagram.com/")
        try:
            self.driver.find_element_by_xpath(self.popup).click()
        except:
            pass