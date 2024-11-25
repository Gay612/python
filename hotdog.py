import math
a=int(input('enter how many peoples:'))
b=int(input('enter how many package of hotdog:'))
c=a*b
d=math.ceil(c/10)
print(d)
e=math.ceil(c/8)
print(e)
f=d*10-c
print(f)
g=d*8-c
print(g)
