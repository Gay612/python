def pattern(n):
    for i in range(1,n+1):
        print(" "* n-i,end=" ")
    for j in range(i,i+1):
        print(j,end= " ")
    print()
n=5
print (pattern(n))
