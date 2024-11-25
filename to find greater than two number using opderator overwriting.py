class a:
    def great(self,n1,n2):
        if n1>n2:
            return n1
        else:
            return n2
class b(a):
    def great(self,n1,n2):
        return max(n1,n2)
y=b()
n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
r=y.great(n1,n2)
print(r)
