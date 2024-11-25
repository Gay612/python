def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
def calc():
 a=int(input('enter your choice:'))
 b=int(input('enter a number:'))
 c=int(input('enter a  number:'))
 if a==1:
    print(add(b,c))
 elif a==2:
    print(sub(b,c))
 elif a==3:
    print(mult(b,c))
 elif a==4:
    print(div(b,c))
 else:
    print('invalid number')
calc()
    
