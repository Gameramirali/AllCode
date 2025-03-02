secend=int(input('secend: '))
if secend%60==0:
    minute=secend//60
    secend=0
else:
    minute=secend//60
    secend=secend%60
    
if minute%60==0:
    hour=minute//60
    minute=0
else:
    hour=minute//60
    minute=minute%60
    
print(f'secend:{secend} ,minute:{minute} ,hour:{hour}')