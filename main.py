from selenium import webdriver
from time import sleep
from Pages.login_page import login
from Pages.home_page import direct_message, post, like_pics, comment, share, respond_dm, watch_stories, like_comments

mobile_emulation = { "deviceName": "iPhone 6/7/8" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options=chrome_options)

class InstaBot:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, pw):
        self.driver.get("https://www.instagram.com/")
        login = Login(self.driver)
        login.login(username, pw)

    def direct_message(self):
        dm = Direct_Message(self.driver)
        dm.direct_message()

    def post(self):
        post = Post(self.driver)
        post.post()

    def like_pics(self):
        like = Like_Pics(self.driver)
        like.like_pics()

    def comment(self):
        comment = Comment(self.driver)
        comment.comment()

    def share(self):
        share = Share_post(self.driver)
        share.share_post()

    def respond(self):
        respond = Respond(self.driver)
        respond.respond()

    def watch_stories(self):
        watch_stories = Watch_Stories(self.driver)
        watch_stories.watch_stories()

    def like_comments(self):
        like_comments = Like_Comments(self.driver)
        like_comments.like_comments()

    def teardown(self):
        self.driver.close()
        self.driver.quit()

matt = InstaBot(driver)
matt.login("username", "pw")

try:
    matt.respond()
    # if no new direct message to respond to: pass:
except:
    pass
matt.comment()
matt.like_comments()
matt.direct_message()
matt.like_pics()
matt.post()
matt.share()
matt.watch_stories()

# look for messages and respond for ~10 min:
count = 0
while count < 30:
    try:
        matt.respond()
        sleep(20)
        count += 1
    except:
        sleep(20)
        count += 1

matt.teardown()