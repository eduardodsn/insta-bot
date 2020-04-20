import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from usuals import UsualFunctions

class Target():
    def __init__(self, driver):
        self.target = str()
        self.num_posts = int()
        self.driver = driver


    # like all posts
    def like_all(self):
        self.driver.get(f'https://www.instagram.com/{self.target}/')
        time.sleep(3)

        num_posts = self.get_num_posts()
        if num_posts > 0:
            print(f'{num_posts} posts to like!')
            for i in range(1, num_posts + 1):
                try:
                    if i == 1:
                        self.open_post()
                    else:
                        self.next_post(i)
                except:
                    UsualFunctions().error(self.driver, 'detect post')
                else:
                    self.like(i)
                    time.sleep(1)
        else:
            print('Maybe this account has no posts to like!')
        
    
    #like some posts
    def like_some(self, num_posts):
        self.driver.get(f'https://www.instagram.com/{self.target}/')
        time.sleep(3)
        profile_posts = self.get_num_posts()

        if num_posts < profile_posts:
            for i in range(1, num_posts+1):
                try:
                    if i == 1:
                        self.open_post()
                    else:
                        self.next_post(i)
                except:
                    UsualFunctions().error(self.driver, 'detect post')
                else:
                    self.like(i)
                    time.sleep(1)
            print(f'{num_posts} posts liked successfully!')
        else:
            UsualFunctions().error(self.driver, 'Number of posts grater than profile number of posts')


    # like a specific post
    def like_one(self, link):
        self.driver.get(link)
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button'))).click()
        except:
            UsualFunctions().error(self.driver, 'like the post')
        else:
            print('Post liked successfully!')

    
    # get number of posts of target profile
    def get_num_posts(self):
        try:
            qnt = UsualFunctions().find_element(self.driver, '/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text
            qnt = qnt.replace('.', '')
            qnt = int(qnt)
        except:
            UsualFunctions().error(self.driver, "like posts")
            return 0
        else:
            if qnt == 0:
                UsualFunctions().error(self.driver, "like posts. Because there's no post to like :/")
                return 0
            else:
                return qnt

    
    #like post
    def like(self, i):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button"))).click()
        except:
            UsualFunctions().error(self.driver, f'like {i}º post')
        else:
            print(f'{i}º post liked successfully!')


    # go to the next post
    def next_post(self, i):
        if i == 2:
            UsualFunctions().click_btn(self.driver, '/html/body/div[4]/div[1]/div/div/a')
        else:
            UsualFunctions().click_btn(self.driver, '/html/body/div[4]/div[1]/div/div/a[2]')


    # open the first post
    def open_post(self):
        UsualFunctions().click_btn(self.driver, '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
