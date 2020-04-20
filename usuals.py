import os
import platform
import getpass
from selenium import webdriver

class UsualFunctions():
    def __init__(self): 
        pass


    # set driver
    def set_driver(self):
        self.system = platform.system().lower()
        if self.system == 'windows':
            return webdriver.Chrome('./chromedriver.exe')
        else:
            return webdriver.Chrome('./chromedriver')

    
    # find element by xpath
    def find_element(self, driver, path):
        try:
            element = driver.find_element_by_xpath(path)
        except:
            self.error(driver, 'find an element')
        else:
            return element


    # click on button
    def click_btn(self, driver, path):
        try:
            btn = self.find_element(driver, path)
            btn.click()
        except:
            pass


    # print error and close driver
    def error(self, driver, my_error):
        driver.close()
        print(f'Error! Impossible to {my_error}! Try again!')

    
    # show the options
    def show_options(self):
        while True:
            print('Select an option bellow:\n"1" - Like all posts in an account\n"2" - Like specific number of posts in an account (starts from the most recent)\n"3" - Like a specific post (needs link)')
            try:
                option = int(input('Enter the option: '))
            except:
                self.clear_terminal()
            else:
                if option not in range(1, 4):
                    self.clear_terminal()
                else:
                    return option

    
    # get credentials
    def get_cred(self):
        user = str(input('Enter your login: '))
        password = getpass.getpass('Enter your password (invisible): ')

        return user, password

    
    # get target account
    def get_target(self):
        target = str(input('Enter the target account: '))
        return target


    # get number of posts to like
    def get_num_posts_to_like(self):
        while True:
            try:
                num_posts = int(input('Enter the number of posts to like: '))
            except:
                self.clear_terminal()
            else:
                if num_posts <= 0:
                    self.clear_terminal()
                else:
                    return num_posts
        

    # get link of the option 3       
    def get_link(self):
        link = str(input('Paste here the post link: '))
        return link


    # clear terminal
    def clear_terminal(self):
        self.system = platform.system().lower()
        if self.system == 'windows':
            os.system('cls')
        else:
            os.system('clear')
    