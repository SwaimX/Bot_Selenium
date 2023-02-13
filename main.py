import datetime
import time, os, json
import threading
import cfg, db, pub_cfg
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

class Instagram():
    def __init__(self, number):
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
        if os.path.exists(f"{cfg.accaunts[f'login{number}']}.ck"):
            print(cfg.accaunts[f'login{number}'])
            for cookie in pickle.load(open(f"{cfg.accaunts[f'login{number}']}.ck", "rb")):
                self.browser.add_cookie(cookie)

            time.sleep(5)
            self.browser.refresh()
            time.sleep(5)

        else:
            time.sleep(5)

            try:
                login = self.browser.find_element(By.XPATH, pub_cfg.auth_login)
                login.send_keys(cfg.accaunts[f'login{number}'])
                password = self.browser.find_element(By.XPATH, pub_cfg.auth_password)
                password.send_keys(cfg.accaunts[f'password{number}'])
                self.browser.find_element(By.XPATH, pub_cfg.auth_btn).click()
                time.sleep(5)
            except:
                print("[!] Incorrect Xpath in authorization")
                self.browser.quit()
                return

            pickle.dump(self.browser.get_cookies(), open(f"{cfg.accaunts[f'login{number}']}.ck", "wb"))
            time.sleep(5)

        print("[+] Login is successful")

    def one_test(self, number):

        i = 1

        while True:
            here = db.bd_sync().check_user_in(cfg.accaunts[f'login{number}'], "batyana")
            if here == "The user here":
                i += 1
                continue
            else:
                break

    def follow_on_followers(self, nick_for_subs, number):
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
                        while True:
                            here = db.bd_sync().check_user_in(cfg.accaunts[f'login{number}'], nick_sub)
                            if here == "The user here":
                                i += 1
                                continue
                            else:
                                db.bd_sync().write_users(cfg.accaunts[f'login{number}'], nick_sub)
                                db.bd_sync().add_nick_name_in_all(nick_sub)
                                print(f"[+]You are subscribed to user {nick_sub} number:{i}")
                                break
                        i += 1
                        time.sleep(cfg.sign_interval)
                    except:
                        print(f"{i} is not work")

                number_of_day -= 1
                self.browser.refresh()
                time.sleep(5)

            elif datetime.datetime.now().hour == 00:
                number_of_day = cfg.number_of_subscriptions_per_day

            else:
                time.sleep(60*60)

    def unsubs_all(self, number):
        self.browser.get(f'https://www.instagram.com/{cfg.accaunts[f"login{number}"]}/following/')
        time.sleep(10)
        i = 1
        while True:
            try:
                self.browser.find_element(By.XPATH, pub_cfg.following(i)).click()
            except :
                time.sleep(cfg.debuging_time)
                print("[!] Incorrect xpath button following")
                self.browser.quit()
                return

            time.sleep(1)

            try:
                self.browser.find_element(By.XPATH, pub_cfg.unsub).click()
            except:
                time.sleep(cfg.debuging_time)
                print("[!] Incorrect xpath button unsubscribe")
                self.browser.quit()
                return

            i += 1
            print("[+]Unsub succesfull")
            time.sleep(cfg.unsub_interval)

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
            thread1 = threading.Thread(target=Instagram(i).follow_on_followers, args=(nick, i))
            thread2 = threading.Thread(target=runnning, args=(i+1,))
            thread1.start()
            thread2.start()
            thread2.join()

        elif to_do == "2":
            Instagram(i).unsubs_all(i)

        elif to_do == "3":
            Instagram(i).unsubs_check_and_time(i)

        elif to_do == "4":
            Instagram(i).check_no_hose(i)

        elif to_do == "5":
            nick = input("Enter a nickname to subscribe to his followers: ")
            threading.Thread(target=Instagram(i).subs_on_user_subs, args=(nick, i)).start()
            threading.Thread(target=Instagram(i).unsubs_check_and_time, args=(i,)).start()
            thread2 = threading.Thread(target=runnning, args=(i + 1,))
            thread2.start()

        elif to_do == "6":
            nick = input("Enter a nickname to subscribe to his followers: ")

        elif to_do == "exit":
            break

        else:
            print("[!]The variant is not True\n"
                  "exit if you want quit\n"
                  "Enter a number from one to five\n")
            continue


if __name__ == "__main__":
    nick = input("Enter a nickname to subscribe to his followers: ")
    Instagram(1).follow_on_followers(nick, 1)
    # runnning(1)





