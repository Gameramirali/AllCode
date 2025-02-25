import random
m=int(input('enter your number: '))
myNumber=random.randint(1,1000)
while True:
    if m==myNumber:
        print('True')
        break
    else:
        print('False')
print(m)