import sqlite3 as sq

with sq.connect('student.db') as con:
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT VARCHAR(50),
    name TEXT,
    surname TEXT,
    birth_year INT,
    score INT
    )''')

    cursor.execute('''INSERT INTO students(hobby,name,surname,birth_year,score)
    VALUES
    ('sewing', 'Alina', 'Karamatova', 1980, 15),
    ('cooking', 'Marina', 'Evseeva', 1985, 12),
    ('swimming', 'Pavel', 'Bibikov', 1983, 9),
    ('football', 'Talant', 'Bolotbekov', 1985, 14),
    ('skiing', 'Irina', 'Kamishanova', 1990, 15),
    ('ice_skating', 'Almaz', 'Aspekov', 1995, 6),
    ('roller_skating', 'Hakim', 'Akramov', 1998, 20),
    ('cooking', 'Farida', 'Mukambetova', 1994, 7),
    ('cooking', 'Karina', 'Kudaiberdieva', 1995, 18),
    ('swimming', 'Nelly', 'Harrison', 1978, 8)''')

    cursor.execute('''SELECT surname FROM students WHERE LENGTH(surname) > 10''')
    for row in cursor:
        print(row)
    cursor.execute('''UPDATE students SET name = 'genius' WHERE score > 10''')

    cursor.execute('''SELECT * FROM students WHERE name LIKE 'genius' ''')
    for row in cursor:
        print(row)


    cursor.execute('''DELETE FROM students WHERE id % 2 = 0 ''')

    cursor.execute('''SELECT * FROM students''')
    for row in cursor:
        print(row)