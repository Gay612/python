n1=int(input('enter ano:'))
n2=int(input('enter ano:'))
n3=int(input('enter ano:'))
if n1>n2 and n2<n3:
     print('True')
elif n1>n2 or n2<n3:
     print('True')
elif not n1 and n2:
     print('true')
else:
    print('invalid no')
