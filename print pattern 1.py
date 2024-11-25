def print_pattern(n):
    number=1
    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        for j in range(1,i+1):
            print(number,end=" ")
            number+=1
        print()
n=4 
print_pattern(n)
   
