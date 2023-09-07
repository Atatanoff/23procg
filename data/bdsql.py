import sqlite3
import res


def get_data():
    with sqlite3.connect(res.data) as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Button (
        id INTEGER PRIMARY KEY,
        button TEXT NOT NULL,
        name TEXT NOT NULL,
        act TEXT NOT NULL
        )''')

    