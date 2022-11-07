#!/usr/bin/env python3
import sqlite3
def query(username: str, password: str):
    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cur.execute('INSERT INTO users VALUES ("admin", "password")')

    query = f"SELECT * FROM users WHERE username = {username!r} AND password = {password!r}"
    print("Query: " + query)

    try:
        res = cur.execute(query).fetchone()
    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")
        return
    print(f"Database result: {res}")

    if res is None:
        print("Wrong credentials")
        return

    username_out, password_out = res

    if username_out != username or password_out != password:
        print("Wrong credentials (are we being hacked?)")
        return

    print(f"Welcome back {username}! The flag is in FLAG.".format(username=username))