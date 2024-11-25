n=int(input('enter a number:'))
sum=0
temp=n
while temp>0:
    a=temp%10
    sum+=a*a*a
    temp=temp//10
if sum==n:
    print('armstrong')
else:
    print('not a armstrong number')
