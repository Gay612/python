n=3
number=1
for i in range(1,n+1):
    for j in range(n-i):
        print('',end=' ')
    for k in range(1,i+1):
        print(number,end=' ')
        number+=1
    print()
for i in range(1,n):
    for j in range(i):
        print('',end=' ')
    for k in range(2,i-1,-1):
        print(number,end=' ')
        number+=1
    print()
    
