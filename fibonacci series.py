n=int(input('enter  a number:'))
a,b=0,1
for i in  range(1,n+1):
    print(a)
    c=a+b
    a=b
    b=c
