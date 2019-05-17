
#!/usr/bin/env python3

import psycopg2

import csv

import pandas as pd

print ("in object_relational_mapper.py")

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(dbname = 'terminal_trader')
        self.cursor     = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        if self.connection:
            if self.cursor:
                self.connection.commit()
                self.cursor.close()
            self.connection.close()

    def create_table(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        self.cursor.execute(
            """CREATE TABLE {table_name}(
                pk SERIAL PRIMARY KEY
            );""".format(table_name = table_name))

    def add_column(self, table_name, column_name, column_type):
        self.cursor.execute(
            """ALTER TABLE {table_name}
                ADD COLUMN {column_name} {column_type}
                ;""".format(table_name = table_name, column_name = column_name, column_type = column_type))

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

    def signup(self, password, balance):
        if does_not_exist(self.username):
            with Database() as db:
                db.cursor.execute(
                """INSERT INTO users(
                        username,
                        password,
                        balance
                    ) VALUES (
                        %s, %s, %s
                    );""", (self.username, password, balance)
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
    with Database() as db:
        tab1 = {"name" : "users",
                "columns" : [
                    {"name":"username",  "type":"VARCHAR"},
                    {"name":"password",  "type":"VARCHAR"},
                    {"name":"balance",   "type":"FLOAT"}]}

        tab2 = {"name" : "transactions",
                "columns" : [
                    {"name":"user_id",           "type":"INTEGER"},
                    {"name":"buy",               "type":"INTEGER"},
                    {"name":"execution_price",   "type":"FLOAT"},
                    {"name":"ticker_symbol",     "type":"VARCHAR"},
                    {"name":"order_quantity",    "type":"INTEGER"},
                    {"name":"time_stamp",        "type":"FLOAT"}]}

        ## TODO Add a functio to the database class, 
        ## to handle for the following statement:
        ## which should be added to the 'tab2' 'tab3':
        ## FOREIGN KEY(user_id) REFERENCES users(pk)

        tab3 = {"name" : "positions",
                "columns" : [
                    {"name":"user_id",           "type":"INTEGER"},
                    {"name":"average_price",     "type":"FLOAT"},
                    {"name":"ticker_symbol",     "type":"VARCHAR"},
                    {"name":"current_holdings",  "type":"INTEGER"}]}


        for table in [tab1, tab2, tab3]:
            db.create_table(table["name"])
            for column_name in table["columns"]:
                db.add_column(
                    table["name"],
                    column_name["name"],
                    column_name["type"])

##    user = User("kyle")
##    print(user.signup("rippere"))

    with User('simbuilder') as u:
        u.signup('opensesame', 1000000.00)


