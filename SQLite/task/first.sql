CREATE TABLE IF NOT EXISTS departments(
department_id integer PRIMARY KEy AUTOINCREMENT,
department_name TEXT
);

CREATE TABLE IF NOT EXISTS employees(
employee_id  INTEGER  PRIMARY KEY  AUTOINCREMENT,
first_name  TEXT NOT NULL,
last_name TEXT NOT NULL,
hire_date  TEXT NOT NULL,
salary  REAL,
department_id integer,
FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE IF NOT EXISTS products (
  product_id INTEGER PRIMARY KEY,
  product_name TEXT NOT NULL,
  price REAL NOT NULL,
  stock_quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phone TEXT NOT NULL
);

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
);

