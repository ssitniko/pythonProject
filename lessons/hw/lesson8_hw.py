import sqlite3 as sq
from http.cookiejar import cut_port_re

with sq.connect('person.db') as con:
    cursor = con.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS departments(
    department_id INTEGER, 
    department_name TEXT VARCHAR(100)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT,
    department_id INT,
    FOREIGN KEY(department_id) REFERENCES departments(department_id)
    )''')

    cursor.execute('''INSERT INTO departments(department_id, department_name)
    VALUES
    (101, 'HR'),
    (102, 'IT'),
    (103, 'Sales')
    ''')

    cursor.execute('''INSERT INTO employees(firstname,lastname,department_id)
    VALUES
    ('Timur', 'Kasimov', 101),
    ('Alina', 'Kasimova', 101),
    ('Gleb', 'Ramazanov', 102),
    ('Marina', 'Narigina', 102),
    ('Ulan', 'Aspekov', 103),
    ('Karina', 'Mambetova', 103)
    ''')
    cursor.execute('''''')

    cursor.execute('''SELECT employees.firstname, employees.lastname, departments.department_name
    FROM employees 
    JOIN departments ON employees.department_id = departments.department_id''')

    for row in cursor:
        print(row)
    print()

    cursor.execute('''SELECT employees.firstname, employees.lastname, departments.department_name
        FROM employees
        JOIN departments ON employees.department_id = departments.department_id WHERE departments.department_name = 'IT' ''')

    for row in cursor:
        print(row)