import sqlite3 
import getpass
import string
import random

conn=sqlite3.connect('password_manager.db')
curser=conn.cursor()

curser.execute("""CREATE TABLE IF NOT EXISTS password(
    website text,
    username text,
    password text
)
""")

curser.execute("""CREATE TABLE IF NOT EXISTS user(
    username text,
    password text
)
""")

def register():
    username=input('username=>')
    password=getpass.getpass('password=>')
    curser.execute('INSERT INTO user(username text,password text) VALUES(?,?);'(username,password))

def login():
    global username
    username=input('username=>')
    password=getpass.getpass('password=>')
    curser.execute('SELECT * FROM user WHERE username=?',(username,))
    user=curser.fetchone()
    if user:
        if password==user[1]:
            print('login')
            return True
    print('Login Failed!')
    return False

def generate_srtong_password(lenght=12):
    pool=string.ascii_lowercase+string.digits+string.punctuation
    password="".join(random.choice(pool) for _ in range(lenght))
    return password
def change_password():
    if not login():
        return
    new_password=getpass.getpass('enter the password =>')
    if not new_password:
        new_password=generate_srtong_password()
        print(f'new strong password is {new_password}')
    curser.execute("""UPDATE user SET password=? WHERE username=?"""(new_password,username))
    print('successfully!')

running=True
while running:
    ask=input('==>')
    if ask=='register':
        register()
    if ask=='login':
        login()
    if ask=='strong password':
        leng=int(input('len password--==>>'))
        generate_srtong_password()
    if ask=="change password":
        change_password()
    if ask=="print":
        curser.execute("SELECT * FROM user;")
    if ask=='exit':
        print("exiting")
        running=False
    conn.commit()
