n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(4-1,0,-1):
        print( ' '*j,end='  ')
for k in range(1,i+1):
        print('*'*i)

