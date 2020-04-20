import time
from target import Target
from usuals import UsualFunctions

class LoginInsta(Target):
    def __init__(self, driver, user, password):
        self.driver = driver
        self.user = user
        self.password = password


    # open instagram page
    def open_page(self):
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/explore/people/suggested/')


    # insert credentials - user
    def insert_user(self):
        time.sleep(2)
        try:
            user_field = UsualFunctions().find_element(self.driver, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
            user_field.click()
            user_field.send_keys(self.user)
        except:
            UsualFunctions().error(self.driver, 'insert login')
    

    # insert credentials - password
    def insert_pass(self):
        try:
            pass_field = UsualFunctions().find_element(self.driver, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
            pass_field.click()
            pass_field.send_keys(self.password)
            UsualFunctions().click_btn(self.driver, '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')
            time.sleep(4)
        except:
            UsualFunctions().error(self.driver, 'insert password')


# login path
def login(user, password):
    # set driver
    driver = UsualFunctions().set_driver()

    # instance & login
    bot = LoginInsta(driver, user, password)
    bot.open_page()
    bot.insert_user()
    bot.insert_pass()
    bot.driver = driver
    return bot
