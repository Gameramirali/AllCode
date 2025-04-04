# برنامه ای بنویسید
# که جدول زیر را ایجاد نماید

# اسم جدول
# Sport

# فیلدهای جدول

# id   name   country    year    olympic   


# SELECT
# SELECT TOP 5
# INSERT INTO
# DELETE FROM
# UPDATE

# مقادیر نام و ... را از ورودی دریافت نماید


import sqlite3

conn = sqlite3.connect('exam2.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Sport(id int, name text, country text, year int, olympic int);')

def Select(table):
    cursor.execute(f'SELECT * FROM {table};')
    for sport in cursor.fetchall():
        print(sport)

def Select_Top(table, number):
    cursor.execute(f'SELECT * FROM {table} LIMIT {number};')
    for sport in cursor.fetchall():
        print(sport)

def Insert(table, id, name, country, year, olympic):
    cursor.execute(f'INSERT INTO {table} VALUES(?,?,?,?,?)', (id, name, country, year, olympic))
    conn.commit()

def Delete(table, field, value):
    cursor.execute(f'DELETE FROM {table} WHERE {field} = ?', (value,))
    conn.commit()

def Update(table, value, where, whereField, whereValue):
    cursor.execute(f'UPDATE {table} SET {where} = ? WHERE {whereField} = ?', (value, whereValue))
    conn.commit()

running = True
while running:
    ask = input('=>')
    if ask == 'select':
        Select('Sport')
    if ask == 'select top':
        number = int(input('Please enter the number of rows you want to view: '))
        Select_Top('Sport', number)
    if ask == 'insert':
        id = int(input('Please enter the id: '))
        name = input('Please enter the name: ')
        country = input('Please enter the country: ')
        year = int(input('Please enter the year: '))
        olympic = int(input('Please enter the olympic value (1 for yes, 0 for no): '))
        Insert('Sport', id, name, country, year, olympic)
    if ask == 'delete':
        field = input('Please enter the field you want to delete (id, name, country, year, olympic): ')
        value = input('Please enter the value: ')
        Delete('Sport', field, value)
    if ask == 'update':
        value = input('Please enter the new value: ')
        where = input('Please enter the field you want to change (id, name, country, year, olympic): ')
        whereField = input('Please enter the field for which to apply the change: ')
        whereValue = input('Please enter the current value: ')
        Update('Sport', value, where, whereField, whereValue)
    if ask == 'Exit':
        print('Exit')
        running = False
