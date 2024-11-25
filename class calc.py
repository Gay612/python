class calc:
    def add(self,num1,num2):
        return(num1+num2)
    def sub(self,num1,num2):
        return(num1-num2)
    def mult(self,num1,num2):
        return(num1*num2)
    def div(self,num1,num2):
        return(num1/num2)
x=calc()
num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
choice=int(input('enter choice number:'))
if  choice==1:
    print(x.add(num1,num2))
elif  choice==2:
    print(x.sub(num1,num2))
elif  choice==3:
    print(x.mult(num1,num2))
elif  choice==4:
    print(x.div(num1,num2))
else:
    print('invalid choice')
    
    
    
    
