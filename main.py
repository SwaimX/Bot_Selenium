import time, threading
import selenium.common.exceptions
import cfg, db
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pickle
#from selenium.webdriver.chrome.options import Options

class Instagram():
    def __init__(self):
        print("lol")
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

        # Auth
        try:
            for cookie in pickle.load(open(f"{cfg.username}.ck", "rb")):
                self.browser.add_cookie(cookie)

            time.sleep(5)
            self.browser.refresh()
            time.sleep(5)

        except:
            time.sleep(5)
            login = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/label/input')
            login.send_keys(cfg.username)
            password = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/label/input')
            password.send_keys(cfg.password)
            self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
            time.sleep(5)

            pickle.dump(self.browser.get_cookies(), open(f"{cfg.username}.ck", "wb"))

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
            except selenium.common.exceptions.NoSuchElementException:
                nick_user = self.browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div[2]/div/div/div/div/a/span/div').text
                db.bd_sync().write_users(cfg.username, nick_user)
                print(f'[+] You subscribe {b} to {nick_user}')
            i += 1
            b += 1
            if i == 50:
                self.browser.refresh()
                i = 1
            time.sleep(60)


    def unsubs_all(self):
        self.browser.get(f'https://www.instagram.com/{cfg.username}/following/')
        time.sleep(10)
        i = 1
        while True:
            self.browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div[3]/button').click()
            time.sleep(1)
            self.browser.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
            i += 1
            time.sleep(60)

    def unsubs_check_time(self):
        for i in range(2):
            uns = db.bd_sync().check_data(cfg.username)
            print(uns)



nick = input('Enter nick: ')
threading.Thread(target=Instagram().unsubs_all()).start()
#threading.Thread(target=Instagram().subs_for_user_subs(nick))


#btn
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[50]/div[3]/button
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[3]/button
#/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]

#msg
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[21]/div[2]/div/div/div/div/div/div/div/div/div
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[17]/div[2]/div/div/div/div/div/div/div/div/div
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[20]/div[2]/div/div/div[1]/div/div/div/div/div/div

#get_nick
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/a/span/div
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/span/a/span/div
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/span/a/span/div

#btn_unsub
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[3]/button
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div[3]/button