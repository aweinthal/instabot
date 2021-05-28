from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from Functions.matt_quotes import rand_quote

class Direct_Message:
    def __init__(self, driver):
        self.driver = driver
        # used xpaths in project as unique IDs usually not available
        self.messages_btn = "/html/body/div[1]/section/nav[1]/div/div/header/div/div[2]/a"
        self.new_msg_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.search_users = "/html/body/div[1]/section/div[2]/div/div[1]/div/div[2]/input"
        self.click_user = "/html/body/div[1]/section/div[2]/div/div[2]/div"
        self.next_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button/div"
        self.message_field = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea"
        self.message_send_btn = "/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button"
        self.popup1 = "/html/body/div[5]/div/div/div/div[3]/button[2]"
        self.popup2 = "/html/body"
        self.info_btn = "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
        self.del_chat_btn = "/html/body/div[1]/section/div[2]/div/div[3]/div[1]/button"
        self.del_confirm = "/html/body/div[4]/div/div/div/div[2]/button[1]"

    def direct_message(self):

        # clear possible popups:
        self.driver.find_element(By.XPATH, self.messages_btn).click()
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup1))
                )
            element.click()
        except:
            pass
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.popup2))
                )
            element.click()
        except:
            pass
        self.driver.find_element(By.XPATH, self.new_msg_btn).click()
        self.driver.find_element(By.XPATH, self.search_users).click()
        # returns random user from a list in class method:
        self.driver.find_element(By.XPATH, self.search_users).send_keys(self.get_to_users())
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.click_user))
                )
            element.click()
        except:
            print("element not found")
        self.driver.find_element(By.XPATH, self.click_user).click()
        self.driver.find_element(By.XPATH, self.next_btn).click()
        # sends a random quote from the direct message quote bank:
        self.driver.find_element(By.XPATH, self.message_field).send_keys(rand_quote("dm"))
        self.driver.find_element(By.XPATH, self.message_send_btn).click()
        self.driver.find_element(By.XPATH, self.info_btn).click()
        # deletes chat to keep next response as correct element for selection:
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.del_chat_btn))
                )
            element.click()
        except:
            print("element not found")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.del_confirm))
                )
            element.click()
        except:
            print("element not found")
        self.driver.get("https://www.instagram.com/")
        

    def get_to_users(self):
        to_users = ['user1','user2','user3']
        return random.choice(to_users)