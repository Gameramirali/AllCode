# name1 = 12
# name2 = 'a'
# name3 = 'reza'

# number = 1


# print(type(number))
# print(type(name1))
# print(type(name2))
# print(type(name3))

# message = """hello world
# How are you?"""
# print(message)


# message = '''He said, "Aren't can't shouldn't wouldn't."'''
# print(message)
# message = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
# print(message)

# message = "he said \"hi\""
# print(message)


# name = "ali"
# family = "rezaei"

# # message = "hello %s%s" % (name, family)
# message = f'hello {name} {family}'

# print(message)

# print('*' + '*' + '*')
# print('*' * 3)

# print(1 + '1')

# x = 1.3

# print(type(x))


# shopping_list = "egg, apple, bread, milk, pen"
# print(shopping_list[10])


# shopping_list = ["egg", "apple", "bread", "milk", "pen"]
# print("first item: ", shopping_list[0])
# print("second item: ", shopping_list[1])
# print("third item: ", shopping_list[2])


# print("before change: ", shopping_list)
# shopping_list[1] = "banana"
# print("after change: ", shopping_list)

# string = "hello"

# new_str = string[:3]
# print(new_str)


# shopping_list = ["egg", "apple", "bread", "milk", "pen", "potato", "tomato"]

# slice_list = shopping_list[0:3]
# slice_list = shopping_list[:3]
# slice_list = shopping_list[1:6:2]

# print(slice_list)


# persons = ['ali', 1, 2, "reza", "mohamad", "javad", "alireza"]
# persons[1] = "tina"


# print(persons[0])
# print(persons[1])
# print(persons[2])
# print(persons[3])
# print(persons[4])
# print(persons[1:4])


# numbers = [1, 2, 3, 4]
# persons = ['a', 'b']

# my_list = [numbers, persons]

# print(my_list[0][0])
# print(my_list[0][1])
# print(my_list[1][0])
# print(my_list[1][1])
# // todo how to access and print just 'a' from my_list


# name = ["ali", "reza", "nima"] + ["matin", "mina"]
# # name = ["ali", "reza", "nima"] - ["ali"] > Type Error

# print(name)


# name = ["ali", "reza", "nima"]
# name.append("hosein")
# name.append(["hosein", "javad"])
# print(name)
# ----------------------------------------------
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers[::2])
# print(numbers[1::2])
# ----------------------------------------------
# numbers=(1,2,3,4,5,6)
# print(numbers(type))
# numbers[3]=-20
# print(numbers)


# numbers=[1,2,3,4,5,6]
# print(numbers[5])
# print(numbers[2:5])
# ----------------------------------------------
# favorite_sports={
#     'sister':'basecketbal',
#     'me':'football',
#     'dad':'swim',
#     'mom':'valiball'
# }
# print(favorite_sports["sister"])
# print(favorite_sports["me"])
# print(favorite_sports["dad"])
# print(favorite_sports["mom"])
# -----------------------------------------------
# shopping_list={
#     'egg',"55"
#     'bread',"20"
# }
# print(shopping_list["bresd"])
# -----------------------------------------------
# students_dict={
#     'id':1,
#     'name':'amirabbas',
#     'ege':'11'
# }
# print('amirabbas id :',students_dict['id'])
# print('amirabbas name :',students_dict['name'])
# print('amirabbas ege :',students_dict['ege'])

# students_list[1 ,'amirabbas', 11]
# print(students_list[0])
# print(students_list[1])
# print(students_list[2])
# ------------------------------------------------
# age=15
# if age>18:
#     print('adult')
#     print('ballala')
# else:
#     print('not adult')
# age=15
# if age>=18:
#     print('adult')
# elif 14<age<18:
#     print('junior')
# else:
#     print('kid')
# ------------------------------------------------
# numbers=50
# if numbers<=50:
#     print('بزرگسال')
# ------------------------------------------------
# age = input('what old are you?')
# if age>=20:
#     print('adult')
# elif 15<age<20:
#     print('junior')
# else:
#     print('kid')

# ------------------------------------------------
# age=input("what old are you?")
# if age>20:
#     print("adult")
# elif 15<age<20:
#     print("juner")
# else:
#     print("kide")

# ------------------------------------------------
# for i in range(8):
#     print("hello")


# string='abcd'
# for a in string:
#     print(a)

# x=range(8)
# print(x)

# nunbers=[1,2,3,4,5,6]
# for x in nunbers:
#     print(x)

# names=['ali','refan']




# x=list(range(10000, 20000))
# print(x)


# even_numbers=x=list(range(10000, 20000, 2))
# print(even_numbers)


# numbers=[1,2,3]
# for one in numbers:
#     for two in numbers:
#         print((one, two))


# result=0
# for numbers in range(10, 21):
#     result=result+numbers

# print("sum of numbers is: ",result)
# ------------------------------------------------
# students_list=0
# for students_list in range(1, 101):
#     print("hello student", students_list)
# ---------------------------------------------------
# people=[]
# while True:
#     name=input('ENTER YOUR NAME TO ADD OR "EXIT" TO EXIT FROM THE APP: ')
#     if name == "exit":
#         print(people)
#         exit()
#     people.append(name)
# ---------------------------------------------------
# import turtle

# screen = turtle.Screen()
# t = turtle.Pen()
# t.pensize(4)
# t.speed('fast')
# color=['brown', 'yellow', 'red', 'Black']


# for j in range(12):
#     t.pencolor(color[j%4])
#     for i in range(4):
#         t.forward(100)
#         t.left(90)
#     t.left(30)


# screen.exitonclick()
# ---------------------------------------------------
# import turtle
# import time

# screen = turtle.Screen()
# screen.bgcolor('orange')
# t = turtle.Pen()
# t.pensize(4)
# t.speed('fast')

# for j in range(12):
#     for i in range(4):
#         t.forward(100)
#         t.left(90)
#     t.left(30)


# screen.exitonclick()

# # تمرین : تغییر رنگ هر یک از مربع ها
# #

#  حلقه while
# people = []

# while True:
#      name = input('enter your name to add or "exit" to exit from the app: ')
#      if name == 'exit':
#          print(people)
#          exit()
#      people.append(name)
# -------------------------------------------------------------------
# b= 20
# n=0
# for a in range(101):
#     n=b+b*a
# print(n)
# -------------------------------------------------------------------
# n=4
# i=0
# b=0
# b=n
# while i<100:
#     b=b+n
#     i=i+1
# print(b)

# numbers=[]
# for i in range(1000,2001):
#     numbers.append(i)
# -------------------------------------------------------------------
# print(numbers[10:71])
# i=1000
# while i < 2001:
#     numbers.append(i)
#     i = i + 1
# print(numbers[10:71])
# -------------------------------------------------------------------
# exercise1 :
# x=int(input('enter a number>'))
# print(x)
# print(type(x))
# output=x
# for i in range(100):
#     output=output+x

# print(output)

# exercise2 :
# even_numbers=[]
# for i in range(1,1001):
#     if i%2==0:
#         even_numbers.append(i)
# print(even_numbers)
# # exercise3 :
# x=int (input('enter your number '))
# for i in range(1000):
#     x=x+1
# print(x)



# exercise4 :
# n=4
# i=0
# b=0
# b=n
# while i<100:
#     print(b)
#     b=b+n
#     i=i+1
# print(b)
# -----------------------------------------------
# n=0
# while n<1001:
#     n=n+2
#     print(n)
# -----------------------------------------------
# x=int(input('enter your number:'))
# z=1
# while z<1000:
#     z=z+1
#     x=x+1
#     print(x)
# ------------------------------------------------
# b=1
# for i in range(5):
#     n=int(input('enter a number:'))
#     b=b*n
# print(b)
# _----------------------------------------------------------
# s=0
# for i in range(5):
#     n=int(input('entera number:'))
#     if n % 2 == 0:
#         s=s+n
# print(s)
        
# ---------------------------------------------------------
# name=[]
# q=0
# while q<5:
#     n=input('enter a name:')
#     name.append(n)
#     q=q+1
# print(name)
# ------------------------------------------------
# for i in range(5):
#     n=input('enter a name:')
#     name.append(n)
# print(name)
# -----------------------------------------------------------
# i=0
# for f in range(5):
#     a=int(input("enter your numbers:"))
#     if a<i:
#         i=a
# print('big your numbers is ',i)


# i=[]
# for d in range(5):
#     n=int(input('anter your name:'))
#     i.append(n)
# s=max(i)
# print('big your number is:',s)
# -----------------------------------------------------------
# i=0
# for f in range(5):
#     a=int(input("enter your numbers:"))
#     if a<i:
#         i=a
# print('big
# -----------------------------------------------------------------------------
# for i in range(66):
#     print("""hello word""")
# ----------------------------------------------------------
# a=input('enter your student:')
# b=int(input('enter python score:'))
# c=int(input('enter app invertor score:'))
# d=int(input('enter scrach score:'))
# e=int((b+c+d)/3)
# print(f"{a}'s avrage is:{e}")
# -------------------------------------------------
# numbers=[1,2,3,4,5,6]
# # i=0
# # while i<len(numbers):
# #     print(i)
# #     i+=1
# import turtle
# s=turtle.Screen()
# p=turtle.Pen()
# s.bgcolor("orange")
# p.ht()
# p.shape("turtle")
# p.pencolor('red')
# p.pensize(4)
# p.penup()
# p.setpos(-88, 0)
# p.pendown()
# p.begin_fill()
# p.fillcolor()
# i=0
# while i<5:
#     p.fd(200)
#     p.right1(144)
# p.end_fill()
# p.penup()
# p.goto(-120, 200)
# p.write("our first python app", font=("Arial", 20, "bold"))

# s.exitonclick()
# ------------------------------------------------------------------
# name=input("what's your name?")
# family=input("what's your family?")
# age=input("what old are you?")
# print(f'hello {name} {family} {age}')or print('hello', name, family, age)
# print('hello', name, family, age)
# ---------------------------------------------------------------
# s=1
# st=5
# for i in range(5):
#     print(' '*s+'* '*st)
#     s=s+1
#     st=st-1
# s=1
# st=5
# i=1
# while i<6:
#     print(' '*s+'* '*st)
#     s=s+1
#     st=st-1
#     i=i+1
# ------------------------------------------------------
# d'
# for i in range(200):
#     print(a)
# ------------------------------------------------------
# one=int(input('enter one number:'))
# phrase=input('Specify the phrase you want between (+_-_/_*) and enter:')
# two=int(input('enter two number:'))
# if phrase=='+':
#     print(one+two)
# if phrase=='-':
#     print(one-two)
# if phrase=='*':
#     print(one*two)
# if phrase=='/':
#     print(one/two)
#----------------------------------------------------------
# i=0
# j=1
# while i<7:
#     if i<7/2:
#         print(' '*(7-2*i)+'* '*(i+1))
#     else:
#         print(' '*(7-2*i)+'* ')
#--------------------------------------------------
# for:
# space=7
# star=1
# for i in range(4):
#     print(' '*space+'* '*star)
#     space-=2
#     star+=2
# while:
# space=7
# star=1
# counter=1
# while counter<5:
#     print(' '*space+'* '*star)
#     space-=2
#     star+=2
#     counter+=1
# ---------------------------------------------
# import random
# w=['1', '1', '1']
# q=list(w)
# def number():
#     if q[:0]==q[:1]==q[:2]:
#         w=str(random.randrange(100,1000))
# q=[]
# q=list(w)
# number()
# print(q)

# import turtle
# s=turtle.Screen()
# s.exitonclic
# import random
# number=randrange(100,1000)
# plater_name=input("helo, what's your name?")
# number_of_guesses=0
# print('okey! '+playernmae+' i am Guessing a number ')
#-----------------------------------
# def number(x):
#     pritn(x)
# number(x)
#-----------------------
#         *
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# star=st1-3-5-7-9
# space=se=9-7-5-3-0
# sr=1
# se=9
# p=1
# while p>5:
#     print(se*' '+sr*'* ')
#     sr+=2
#     se-=2
#     p+=1
#------------------------------
# import tkinter as tk
# from tkinter import ttk


# def submit():
#     print(user_name.get())


# root = tk.Tk()
# root.geometry("600x400")
# root.resizable(False, False)

# main_frame = ttk.Frame(root)
# main_frame.pack()

# user_name_label = ttk.Label(
#     main_frame, text="user name", font=14, padding=(0, 0, 10, 0))
# user_name_label.pack(side="left")
# user_name = ttk.Entry(main_frame, font=14, foreground="red")
# user_name.pack(side="left")

# buttons_frame = ttk.Frame(root)
# buttons_frame.pack()

# submit_button = ttk.Button(
#     buttons_frame, text="Submit", command=submit, padding=10)
# submit_button.pack(side="left", padx=10, pady=10)
# quit_button = ttk.Button(buttons_frame, text="quit",
#                          command=root.destroy, padding=10)
# quit_button.pack(side="left", padx=10, pady=10)


# root.mainloop()
#-----------------------------------------------
# n = int(input('enter your nmber>'))
# while n:
#     print(n % 10)
#     n=n // 10
#"""
# 1-عدد را در یافت می کنیم
# 2-بعد داخل حلقه که به تعداد ارقام متغیر ان هست می نویسیم چاپ کنه باقیمانده ان در 10 و بعد ان را تغسیم بر 10 می کنیم
#"""
#-----------------------------------------------------

# from tkinter import *
# class Calculator:




#     def __init__(self, master):
#         self.master = master
#         master.title("Python Calculator")
#         self.equation=Entry(master, width=36, borderwidth=5)
#         self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#         self.createButton()


# 'equl'

#     def createButton(self):
#         b1 = self.addButton(1)
#         b2 = self.addButton(2)
#         b3 = self.addButton(3)
#         b4 = self.addButton(4)
#         b5 = self.addButton(5)
#         b6 = self.addButton(6)
#         b7 = self.addButton(7)
#         b8 = self.addButton(8)
#         b9 =  self.addButton(9)
#         b_add = self.addButton('+')
#         b_sub = self.addButton('-')
#         b_mult = self.addButton('*')
#         b_div = self.addButton('/')
#         b_clear = self.addButton('c')
#         b_equal = self.addButton('=')
#         row2=[b4,b5,b6,b_sub]
#         row3=[b1,b2,b3,b_mult]
#         row4=[b_clear,b0,b_equal,b_div]
#         r=1
#         for row in [row1, row2, row3, row4]:
#             c=0
#             for buttn in row:
#                 buttn.grid(row=r, column=c, columnspan=1)
#                 c+=1
#             r+=1
#     def addButton(self,value):
#             return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))
#     def clickButton(self, value):
#         current_equation=str(self.equation.get())
#         if value == 'c':
#             self.equation.delete(-1, END)
#         elif value == '=':
#             answer = str(eval(current_equation))
#             self.equation.delete(-1, END)
#             self.equation.insert(0, answer)
#         else:
#             self.equation.delete(0, END)
#             self.equation.insert(-1, current_equation+value)
# if __name__=='__main__':
#     root = Tk()
#     my_gui = Calculator(root)
#     root.mainloop()
# ----------------------------------
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
