from calendar import c
import sqlite3 

conn=sqlite3.connect('./task3.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS customer(
    id int,
    name text,
    family text,
    phone int,
    address text,
    city text
)
''')

ask=input('=>')
if ask=='insert':
    for i in range(1,3):
        id=i
        name=input('name: ')
        family=input('family: ')
        phone=int(input('phone number: '))
        address=input('address: ')
        city=input('city: ')
        cursor.execute('INSERT INTO customer(id,name,family,phone,address,city) VALUES(?,?,?,?,?,?)',(id,name,family,phone,address,city))
cursor.execute("SELECT city FROM customer WHERE city='tehran'")
print('hello')

conn.commit()