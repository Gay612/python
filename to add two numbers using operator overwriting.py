class a:
    def add(self,n1,n2):
        return n1+n2
class b(a):
    def add(self,n1,n2):
        return n1+n2
y=b()
n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
r=y.add(n1,n2)
print(r)
