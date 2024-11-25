n=int(input('enter a number:'))
a=65

for i in range(n):
     for j in range (i+1):
         b=chr(a)
         print(b,end='')
     a+=1
     print( )
