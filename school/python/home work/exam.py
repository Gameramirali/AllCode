# 1-1
# name=input('enter your name: ')
# print(name[::-1])
# 1-2
# name="alireza"
# finally1=""
# for i in name:
#     finally1 = i + finally1

# print(finally1)

# 2

# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

x=1
y=''
for i in range(1,6):
    print(f'{y}{str(x)}')
    y+=str(x)+' '
    x+=1