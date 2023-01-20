import time, threading
import selenium.common.exceptions
import cfg, db, pub_cfg
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

class Instagram():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        #options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.get('https://www.instagram.com/')
        time.sleep(5)
        try:
            self.browser.find_element(By.XPATH, pub_cfg.cookies_accept).click()
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
            login = self.browser.find_element(By.XPATH, pub_cfg.auth_login)
            login.send_keys(cfg.username)
            password = self.browser.find_element(By.XPATH, pub_cfg.auth_password)
            password.send_keys(cfg.password)
            self.browser.find_element(By.XPATH, pub_cfg.auth_btn).click()
            time.sleep(5)

            pickle.dump(self.browser.get_cookies(), open(f"{cfg.username}.ck", "wb"))

    def subs_on_user_subs(self, nick_for_subs):
        self.browser.get(f'https://www.instagram.com/{nick_for_subs}/followers/')
        i = 1
        b = 1
        time.sleep(5)

        while True:
            sub = self.browser.find_element(By.XPATH, pub_cfg.sub_subscribeb(i))
            sub.click()
            time.sleep(2)
            try:
                self.browser.find_element(By.XPATH, pub_cfg.sub_cancel).click()
                b -= 1
                print('You now subscribe')

            except:
                nick_user = self.browser.find_element(By.XPATH, pub_cfg.sub_nick(i)).text
                db.bd_sync().write_users(cfg.username, nick_user)
                db.bd_sync().add_nick_name_in_all(nick_user)
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

    def unsubs_check_and_time(self):
        while True:
            uns = db.bd_sync().check_data(cfg.username)
            time.sleep(2)
            if uns != None:
                print(uns)
                self.browser.get(f'https://www.instagram.com/{uns}/')
                time.sleep(5)
                self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
                time.sleep(5)
                self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[7]').click()
                db.bd_sync().remove_nickname(cfg.username, uns)
                time.sleep(60)
            else:
                time.sleep(60*60)





nick = input('Enter nick: ')
Instagram().subs_on_user_subs(nick)
#Instagram().unsubs_check_and_time()
#threading.Thread(target=Instagram().unsubs_check_and_time()).start()
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

#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[7]