import sqlite3

conn=sqlite3.connect('task.db')
cursor=conn.cursor()

# 1:
# cursor.execute('CREATE TABLE IF NOT EXISTS Student(Name Text,Age Intiger,Class Intiger)')
# for i in range(4):
#     Name=input('Enter your name->')
#     Age=int(input('Enter your age->'))
#     Class=input('Enter your Class->')
#     cursor.execute('INSERT INTO Student(Name,Age,Class) VALUES(?,?,?)',(Name,Age,Class))
# cursor.execute('INSERT INTO Student(Name,Age,Class) VALUES("reza","15","10")')
# cursor.execute("SELECT * FROM Student")
# for i in cursor.fetchall():
#     print(i)
# conn.commit()
# 2:
# cursor.execute('CREATE TABLE IF NOT EXISTS Book(Title Text,Author Text,Pages Intiger);')
# Title=input('Title: ')
# Author=input('Author: ')
# Pages=input('Pages: ')
# cursor.execute('INSERT INTO Book(Title,Author,Pages) VALUES(?,?,?)',(Title,Author,Pages))
# cursor.execute('INSERT INTO Book(Title,Author,Pages) VALUES("جاوا برای مبتدیان","janatan","300")')
# cursor.execute("SELECT * FROM Book")
# for i in cursor.fetchall():
#     print(i)
# conn.commit()
# 3:
# cursor.execute('CREATE TABLE IF NOT EXISTS Products(Name Text,Price Intiger);')
# Name=input('Name: ')
# Price=int(input('Price: '))
# cursor.execute('INSERT INTO Products(Name,Price) VALUES(?,?)',(Name,Price))
# cursor.execute("SELECT * FROM Products")
# for i in cursor.fetchall():
#     print(i)
# conn.commit()