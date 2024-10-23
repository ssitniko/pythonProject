import sqlite3 as sq

with sq.connect('first.db') as con:
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT VARCHAR(100),
    sex TEXT VARCHAR(6),
    old INTEGER,
    score INTEGER
    )''')

    cursor.execute('''INSERT INTO user(name,sex,old,score)
    VALUES
    ('aleks','male',30,50),
    ('bob','male',35,60),
    ('bil','male',37,25),
    ('mary','female',23,75)''')

    cursor.execute('''SELECT * FROM user''')


