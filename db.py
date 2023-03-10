import sqlite3, datetime
class bd_sync():
    try:
        def __init__(self):

            self.db = sqlite3.connect('swaim.db')
            self.c = self.db.cursor()

        def write_users(self, my_nick, nick_subs):

            try:
                self.c.execute(f"INSERT INTO {my_nick}_inf VALUES ('{nick_subs}', '{datetime.datetime.now().date()}');")

            except sqlite3.OperationalError:
                self.c.execute(f'''CREATE TABLE {my_nick}_inf (nick_you_sub text, data text);''')
                self.c.execute(f"INSERT INTO {my_nick}_inf VALUES ('{nick_subs}', '{datetime.datetime.now().date()}');")

            self.db.commit()
            self.db.close()

        def check_data(self, my_nick):

            select_all_rows = f"SELECT * FROM {my_nick}_inf"
            self.c.execute(select_all_rows)
            rows = self.c.fetchall()
            for row in rows:
                day = row[1]
                day = day.split('-')
                if int(day[2]) > datetime.datetime.now().day + 2:
                    self.db.close()
                    return row[0]
            self.db.close()
            return None


        def remove_nickname(self, my_nick, nick_remove):
            self.c.execute(f"DELETE FROM {my_nick}_inf WHERE nick_you_sub = '{nick_remove}'")
            self.db.commit()
            self.db.close()

        def add_nick_name_in_all(self, nick):
            while True:
                try:
                    select_all_rows = "SELECT * FROM subs_inf"
                    self.c.execute(select_all_rows)
                    rows = self.c.fetchall()
                    for row in rows:
                        nick_in_data = row[0]
                        if nick_in_data == nick:
                            self.db.close()
                            return
                    self.c.execute(f"INSERT INTO subs_inf VALUES ('{nick}', true);")
                    self.db.commit()
                    self.db.close()
                    return

                except:
                    self.c.execute('CREATE TABLE subs_inf (nick text, hose BOOLEAN);')
                    self.db.commit()
                    continue

        def not_hose(self, nick):
            self.c.execute(f"UPDATE subs_inf SET hose = false WHERE nick = '{nick}'")
            self.db.commit()
            self.db.close()


    except:
        print("[!] Data base error")




