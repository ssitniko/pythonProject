import sqlite3 as sq

cars = [
    ('Audi', 555),
    ('Mercedes', 777),
    ('Skoda', 444),
    ('Volvo', 222),
    ('Bentley', 333),

]

with sq.connect('cars.db') as con:
    cursor = con.cursor()

    cursor.executescript('''CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER)
    ''')
    cursor.executemany('''INSERT INTO cars VALUES(NULL, ?, ?)''', cars)
    cursor.execute('SELECT model, price FROM cars')
    rows = cursor.fetchall()
    print(rows)
