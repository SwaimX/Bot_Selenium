import sqlite3, datetime
class bd_sync():
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
                return row[0]
        return None




