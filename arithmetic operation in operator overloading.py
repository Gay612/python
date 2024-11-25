class a:
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def mult(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        return n1/n2
class b(a):
    def abc(self,n1,n2):
        return n1,n2
x=b()
n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
a=int(input("Enter your choice:"))
if a==1:
    print(x.add(n1,n2))
elif a==2:
    print(x.sub(n1,n2))
elif a==3:
    print(x.mult(n1,n2))
elif a==4:
    print(x.div(n1,n2))
    
        

