import sqlite3
# def Select():
# 	query='SELECT * FROM employee'
# 	curser.execute(query)
#     print(curser.fetchall())
# 	conn.commit()

def insert_int_table(**kwargs):
	print(kwargs.get("id"))
	print(kwargs.get("name"))

try:
	conn=sqlite3.connect('mian.db')
	curser=conn.cursor()
	# Select()
	insert_int_table(id=5,name='sadra',family='vali',email='sadra2@gmail.com')
except sqlite3.Error:
	print(f'Error{sqlite3.Error}')

print('amirali')