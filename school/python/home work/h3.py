num1=input('number (lenght=3): ')
mylist=[]
myfinally=0

for i in num1:
    mylist.append(int(i))
    
for i in mylist:
    myfinally+=i
    
print(myfinally)