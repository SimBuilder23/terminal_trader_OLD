
#!/usr/bin/env python3

import csv
import pandas as pd

from orm import Database

def does_not_exist(username):
    with Database() as db:
        db.cursor.execute(
            "SELECT username FROM users WHERE username=%s;", (username,))
        occurences = db.cursor.fetchall()
        if len(occurences) < 1:
            print("occurences", occurences, type(occurences))
            return True
        else:
            print("username taken")
            return False

class User:

    def __init__(self, username):
        self.username = username

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        pass


    def login(self, password):
        with Database() as db:
            db.cursor.execute(
                """SELECT password
                    FROM users
                    WHERE username=%s;""",
                    (self.username,))
            if password == db.cursor.fetchone():
                return True
            else:
                return False


    def signup(self, password):
        if does_not_exist(self.username):
            with Database() as db:
                db.cursor.execute(
                """INSERT INTO users(
                        username,
                        password
                    ) VALUES (
                        %s, %s
                    );""", (self.username, password)
                )
                return True
        else:
            return False

    def buy(self, ticker_symbol, trade_volume):
        # FIXME
        pass

    def sell(self):
        # TODO
        pass

if __name__ == "__main__":
    user = User("kyle")
    print(user.signup("rippere"))




