import time
from threading import Thread
import cfg, db, pub_cfg
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

class Instagram():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
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
            print("[+]Unsub succesfull")
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

    def check_no_hose(self):
        self.browser.get(f'https://www.instagram.com/{cfg.username}/followers/')
        time.sleep(15)
        gor = 0
        i = 1
        while True:

            try:
                nick_no_hose = self.browser.find_element(By.XPATH, pub_cfg.hose_no(i)).text
                time.sleep(1)
                self.browser.find_element(By.XPATH, pub_cfg.hose_for_scroll(i)).click()
                time.sleep(1)
                self.browser.find_element(By.XPATH, pub_cfg.hose_for_cancel).click()
                db.bd_sync().add_nick_name_in_all(nick_no_hose)
                db.bd_sync().not_hose(nick_no_hose)
                i += 1
                gor = 0

            except:
                gor += 1
                if gor == 15:
                    print('[+] Finally')
                    return
                else:
                    time.sleep(15)
                    continue







if __name__ == "__main__":
    while True:
        to_do = input("1.Follow all followers of the account\n"
                      "2.Unsubscribe from everyone\n"
                      "3.Unsubscribe if more than two days have passed\n"
                      "4.Checking accounts for mutual subscription\n"
                      "5.Optimal\n"
                      "What to do: ")
        if to_do == "1":
            nick = input("Enter a nickname to subscribe to his followers: ")
            Instagram().subs_on_user_subs(nick)

        elif to_do == "2":
            Instagram().unsubs_all()

        elif to_do == "3":
            Instagram().unsubs_check_and_time()

        elif to_do == "4":
            Instagram().check_no_hose()

        elif to_do == "5":
            nick = input("Enter a nickname to subscribe to his followers: ")
            Thread(target=Instagram().unsubs_check_and_time()).start()
            Thread(target=Instagram().subs_on_user_subs, args=nick)
            Thread(target=Instagram().check_no_hose())

        elif to_do == "exit":
            break

        else:
            print("[!]The variant is not True\n"
                  "exit if you want quit\n"
                  "Enter a number from one to five\n")
            continue





