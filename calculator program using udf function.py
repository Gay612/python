def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter your choice:'))
if c==1:
    print(add(a,b))
elif c==2:
    print(sub(a,b))
elif c==3:
    print(mult(a,b))
elif c==4:
    print(div(a,b))
else:
    print('invalid')


