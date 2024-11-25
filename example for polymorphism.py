class bird:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class dog:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class cat:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
a=bird('parrot')
b=dog('lika')
c=cat('kitty')
for  i in (a,b,c):
    i.var()
   

