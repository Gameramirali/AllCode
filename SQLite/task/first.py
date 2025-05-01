import sqlite3

conn=sqlite3.connect('first.db')
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS departments(
department_id integer PRIMARY KEy AUTOINCREMENT,
department_name TEXT
);    
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
  product_id INTEGER PRIMARY KEY,
  product_name TEXT NOT NULL,
  price REAL NOT NULL,
  stock_quantity INTEGER NOT NULL
);               
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phone TEXT NOT NULL
);  ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    employee_id  INTEGER  PRIMARY KEY  AUTOINCREMENT,
    first_name  TEXT NOT NULL,
    last_name TEXT NOT NULL,
    hire_date  TEXT NOT NULL,
    salary  REAL,
    department_id integer,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
  sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  employee_id INTEGER NOT NULL,
  sale_date DATE NOT NULL,
  sale_amount REAL NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products (product_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
  FOREIGN KEY (employee_id) REFERENCES dates (employee_id)
)               
''')

cursor.execute('''INSERT INTO products(product_id,product_name,price,stock_quantity) 
VALUES(3,kala,16000,5)''')

conn.commit()
conn.close()