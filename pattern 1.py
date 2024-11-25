a=int(input('enter a no:'))
for i in range(a):
    if i==0 or i==a-1:
        print(        '*'      )
    elif i==1 or i==a-2:
        print('*'               '*')
    else:
        print(         '*')
