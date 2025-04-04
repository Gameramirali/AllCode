import sqlite3

conn = sqlite3.connect('exam1.db')
cursor = conn.cursor()

# 1
cursor.execute('''CREATE TABLE IF NOT EXISTS Shipper
                  (ShipperID, ShipperName TEXT, Phone TEXT)''')

shippers = [
    (1, 'Sara', '123-456-7890'),
    (2, 'Alex', '234-567-8901'),
    (3, 'John', '345-678-9012'),
    (4, 'Mia', '456-789-0123'),
    (5, 'Emma', '567-890-1234')
]

for shipper in shippers:
    cursor.execute('INSERT INTO Shipper VALUES (?, ?, ?)', shipper)

cursor.execute("SELECT * FROM Shipper WHERE ShipperName = 'Sara'")
print(cursor.fetchall())

# 2
cursor.execute('''CREATE TABLE IF NOT EXISTS Category
                  (CategoryID, CategoryName TEXT, Description TEXT)''')

categories = [
    (1, 'Electronics', 'Devices and gadgets'),
    (2, 'Clothing', 'Apparel and accessories'),
    (3, 'Books', 'Printed and digital books')
]

for category in categories:
    cursor.execute('INSERT INTO Category VALUES (?, ?, ?)', category)

cursor.execute("SELECT * FROM Category")
print(cursor.fetchall())

conn.commit()
