def fibo(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
for i in fibo(10):
        print(i)
