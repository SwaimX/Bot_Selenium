import sqlite3

class bd_sync():
    def __init__(self):
        self.db = sqlite3.connect('swaim.db')
        self.c = self.db.cursor()

    def write_users(self, my_nick, nick_subs):
        try:
            self.c.execute(f"INSERT INTO {my_nick} VALUES ('{nick_subs}');")
        except sqlite3.OperationalError:
            self.c.execute(f'''CREATE TABLE {my_nick} (nick_you_sub text);''')
            self.c.execute(f"INSERT INTO {my_nick} VALUES ('{nick_subs}');")
        self.db.commit()
        self.db.close()



