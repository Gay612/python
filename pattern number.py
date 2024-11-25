n=int(input("enter a number:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
for i in range(1,n):
    for j in range(i):
        print( " " ,end="")
    for k in range(n-1,0,1):
        print(num,end="")
        num+=1
    print()
        
        
