# SQL -
# datbase -
# СУБД - система управления БазДанных
# relation - norelation
# CRUD - create read update delete

import sqlite3 as sq

with sq.connect('test.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR(100),
    old INT DEFAULT 0
    ) ''')
    cursor.execute('''INSERT INTO users(fio,old)
     VALUES
     ('Bekbolo',60),
     ('beka',123)''')
    #     CREATE
    cursor.execute('''SELECT fio,old FROM users''')

    # for row in cursor:
    #     print(row)
# read

