import sqlite3

conn=sqlite3.connect('task2.db')
curser=conn.cursor()

curser.execute('''
               CREATE TABLE IF NOT EXISTS Product(
                   id int,
                   name text,
                   price real,
                   weight int,
                   campany text,
                   country text
               )
               ''')

running=True
while running:
    ask=input('->')
    if ask=='exit':
        print('exiting')
        running=False
    if ask=='insert':
        curser.execute('''
                        INSERT INTO Product ( id, name, price, weight, campany, country )
                        VALUES
                        ( 1, 'TV', 25000, 48, 'Samsung', 'Korea' ),
                        ( 2, 'Fridge', 256.999, 40, 'LG', 'Korea' ),
                        ( 3, 'Mobile', 2000, 20, 'Xiaomi', 'China' ),
                        ( 4, 'Dishwasher', 29652, 7856, 'LG', 'Korea' ),
                        ( 5, 'LapTop', '145543486', '1465', 'ASUS', 'Taiwan' );''')
    conn.commit()