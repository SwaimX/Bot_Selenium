import datetime
import time, os
import threading
import cfg, db, pub_cfg
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

class Instagram():
    def __init__(self, number):
        self.your_nick = cfg.accaunts[f"login{number}"]
        self.your_password = cfg.accaunts[f"password{number}"]
        try:
            options = webdriver.ChromeOptions()
            options.headless = cfg.visible
            self.browser = webdriver.Chrome(options=options)

        except:
            options = webdriver.FirefoxOptions()
            options.headless = cfg.visible
            self.browser = webdriver.Firefox(options=options)


        self.browser.get('https://www.instagram.com/')
        time.sleep(5)
        try:
            self.browser.find_element(By.XPATH, pub_cfg.cookies_accept).click()
            print("[+] Cookies accept")
        except:
            print("[+]Cokies dont need")

        # Auth
        if os.path.exists(f"{self.your_nick}.ck"):
            for cookie in pickle.load(open(f"{self.your_nick}.ck", "rb")):
                self.browser.add_cookie(cookie)

            time.sleep(5)
            self.browser.refresh()
            time.sleep(5)

        else:
            time.sleep(5)

            try:
                login = self.browser.find_element(By.XPATH, pub_cfg.auth_login)
                login.send_keys(self.your_nick)
                password = self.browser.find_element(By.XPATH, pub_cfg.auth_password)
                password.send_keys(self.your_password)
                self.browser.find_element(By.XPATH, pub_cfg.auth_btn).click()
                time.sleep(5)
            except:
                print(f"[!][{self.your_nick}] Incorrect Xpath in authorization")
                self.browser.quit()
                return

            pickle.dump(self.browser.get_cookies(), open(f"{self.your_nick}.ck", "wb"))
            time.sleep(5)

        print("[+] Login is successful")

    def follow_on_followers(self, nick_for_subs):
        time.sleep(5)

        number_of_day = cfg.number_of_subscriptions_per_day

        self.browser.get(f'https://www.instagram.com/{nick_for_subs}/followers/')
        time.sleep(5)
        while True:
            if number_of_day != 0:
                follow_buttons = self.browser.find_elements(By.XPATH, "//*[@class='_acan _acap _acas _aj1-']")
                nick_subers = self.browser.find_elements(By.XPATH, "//*[@class=' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")

                i = 0

                for button in follow_buttons:
                    try:
                        nick_sub = nick_subers[i].text
                        button.click()
                        time.sleep(3)
                        try:
                            self.browser.find_element(By.XPATH, pub_cfg.sub_cancel).click()
                            print(f'[{self.your_nick}]You now subscribe')
                        except:
                            while True:
                                here = db.bd_sync().check_user_in(self.your_nick, nick_sub)
                                if here == "The user here":
                                    i += 1
                                    continue
                                else:
                                    db.bd_sync().write_users(self.your_nick, nick_sub)
                                    db.bd_sync().add_nick_name_in_all(nick_sub)
                                    print(f"[+][{self.your_nick}]You are subscribed to user {nick_sub} number:{i}")
                                    break

                            time.sleep(cfg.sign_interval)
                        i += 1
                    except:
                        print(f"[{self.your_nick}] {i} is not work")

                number_of_day -= 1
                self.browser.refresh()
                time.sleep(5)

            elif datetime.datetime.now().hour == 00:
                number_of_day = cfg.number_of_subscriptions_per_day

            else:
                time.sleep(60*60)

    def unsubs_all(self):
        self.browser.get(f'https://www.instagram.com/{self.your_nick}/following/')
        time.sleep(10)

        while True:
            unfollow_buttons = self.browser.find_elements(By.XPATH, "//*[@class='_acan _acap _acat _aj1-']")
            text_of_nickname = self.browser.find_elements(By.XPATH, "//*[@class=' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")

            i = 0
            if str(unfollow_buttons) != "[]":
                for element in unfollow_buttons:
                    try:
                        element.click()
                        nick = text_of_nickname[i].text
                        time.sleep(3)
                        self.browser.find_element(By.XPATH, pub_cfg.unsub).click()
                        try:
                            db.bd_sync().remove_nickname(self.your_nick, nick)
                        except:
                            pass
                        print(f"[+][{self.your_nick}] You unsub {nick} ")
                        i += 1
                        time.sleep(cfg.unsub_interval)
                    except:
                        pass

                self.browser.refresh()

            else:
                print(f'[+] Account {self.your_nick} unsubscribed from everyone')
                self.browser.quit()
                return



    def unsubs_check_and_time(self, number):
        while True:
            uns = db.bd_sync().check_data(cfg.accaunts[f'login{number}'])
            time.sleep(2)
            if uns != None:
                print(uns)
                self.browser.get(f'https://www.instagram.com/{uns}/')
                time.sleep(5)
                try:
                    self.browser.find_element(By.XPATH, pub_cfg.followingser).click()
                    time.sleep(5)
                except:
                    time.sleep(cfg.debuging_time)
                    print("[!] Incorrect xpath button following")
                    self.browser.quit()
                    return

                try:
                    self.browser.find_element(By.XPATH, pub_cfg.unsubs).click()
                except:
                    time.sleep(cfg.debuging_time)
                    print("[!] Incorrect xpath button unsubscribe")
                    self.browser.quit()
                    return

                db.bd_sync().remove_nickname(cfg.accaunts[f'login{number}'], uns)
                time.sleep(60)
            else:
                time.sleep(60*60)

    def check_no_hose(self, number):
        self.browser.get(f'https://www.instagram.com/{cfg.accaunts[f"login{number}"]}/followers/')
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




def runnning(i):
    while True:
        to_do = input("1.Follow all followers of the account\n"
                      "2.Unsubscribe from everyone\n"
                      "3.Unsubscribe if more than two days have passed\n"
                      "4.Checking accounts for mutual subscription\n"
                      "5.Optimal\n"
                      "What to do: ")
        if to_do == "1":
            nick = input("Enter a nickname to subscribe to his followers: ")
            thread1 = threading.Thread(target=Instagram(i).follow_on_followers, args=(nick))
            thread2 = threading.Thread(target=runnning, args=(i+1,))
            thread1.start()
            thread2.start()
            thread2.join()

        elif to_do == "2":
            Instagram(i).unsubs_all()

        elif to_do == "3":
            Instagram(i).unsubs_check_and_time(i)

        elif to_do == "4":
            Instagram(i).check_no_hose(i)

        elif to_do == "5":
            nick = input("Enter a nickname to subscribe to his followers: ")
            threading.Thread(target=Instagram(i).follow_on_followers, args=(nick, )).start()
            threading.Thread(target=Instagram(i).unsubs_check_and_time, args=(i,)).start()
            thread2 = threading.Thread(target=runnning, args=(i + 1,))
            thread2.start()

        elif to_do == "exit":
            break

        else:
            print("[!]The variant is not True\n"
                  "exit if you want quit\n"
                  "Enter a number from one to five\n")
            continue


if __name__ == "__main__":
    # nick = input("Enter a nickname to subscribe to his followers: ")
    # Instagram(1).unsubs_all(1)
    runnning(1)





