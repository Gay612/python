def var(n):
    return lambda a,b:a+b+n
b=var(5)
print(b(5,5))
