import time
import cfg
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.chrome.options import Options

class Instagram():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.get('https://www.instagram.com/')
        #self.browser.get('https://www.youtube.com/')
        time.sleep(5)
        try:
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
            print("[+] Cookies accept")
        except:
            print("[+]Cokies dont need")

        #Auth
        time.sleep(5)
        login = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/label/input')
        login.send_keys(cfg.username)
        password = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/label/input')
        password.send_keys(cfg.password)
        self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
        time.sleep(5)

    def subs_for_user_subs(self, nick_for_subs):
        self.browser.get(f'https://www.instagram.com/{nick_for_subs}/followers/')
        i = 1
        b = 1
        time.sleep(5)
        while True:
            sub = self.browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div[3]/button')
            sub.click()
            time.sleep(2)
            try:
                self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
                b -= 1
                print('You now subscribe')
            except:
                print(f'[+] You subscribe {b} users')
            i += 1
            b += 1
            if i == 50:
                self.browser.refresh()
                i = 1
            time.sleep(60)



        #time.sleep(10)

Instagram().subs_for_user_subs('therock')

#btn
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[50]/div[3]/button
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[3]/button
#/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]

#msg
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[21]/div[2]/div/div/div/div/div/div/div/div/div
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[17]/div[2]/div/div/div/div/div/div/div/div/div
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[20]/div[2]/div/div/div[1]/div/div/div/div/div/div