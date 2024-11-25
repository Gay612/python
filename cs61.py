n=int(input('enter a number:'))
for i in range(1,n+1):
     for j in range(4,i,-1):
         print(' ',end='')
         for k in range(i+1):
             print(k,end=' ')
         print()
