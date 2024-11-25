n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
n3=int(input('enter a number:'))
if n1>n2 and n1>n3:
    print(n1,'is the greatest number')
elif n2>n1 and n2>n3:
    print(n2,'is the greatest number')
else:
    print(n3,'is the greatest number')
