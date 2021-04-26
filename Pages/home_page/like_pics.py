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