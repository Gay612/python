def var(n):
    if n<=1:
        return 1
    else:
        return n +var(n-1)
n=int(input('enter a number:'))
print('the sum of natural number is',var(n))
