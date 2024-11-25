def var(n):
   
    if n<=1:
        return n
       
    else:
        return n+var(n-1)
n=int(input('enter a no:'))

print('the sum is',var(n))
