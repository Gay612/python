def var(x):
    def abc(y):
        return x+y
    return abc
add=var(15)
print(add(10))
