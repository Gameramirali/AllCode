import sqlite3
from itertools import product
import random

# اتصال به دیتابیس
conn = sqlite3.connect("unique_test.db")
cursor = conn.cursor()

# ایجاد جدول
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    ContactName TEXT,
    Address TEXT,
    City TEXT,
    PostalCode TEXT,
    Country TEXT
)
""")

# داده‌های اولیه برای ترکیب
names = ["John", "Alice", "Robert", "Emily", "Michael"]
contact_names = ["Smith", "Johnson", "Brown", "Davis", "Garcia"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
countries = ["USA", "Canada", "UK", "Germany", "Australia"]

# تولید ترکیب‌های منحصر به فرد
unique_combinations = list(product(names, contact_names, cities, countries))
random.shuffle(unique_combinations)  # ترتیب را به‌طور تصادفی تغییر می‌دهیم

# افزودن حداکثر ۱۰۰ رکورد
for i in range(100):
    name, contact_name, city, country = unique_combinations[i]
    address = f"{random.randint(1, 999)} Main St"
    postal_code = f"{random.randint(10000, 99999)}"
    cursor.execute("INSERT INTO Users (Name, ContactName, Address, City, PostalCode, Country) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, contact_name, address, city, postal_code, country))

# ذخیره و بستن اتصال
conn.commit()
conn.close()

print("Database with unique records created successfully!")
