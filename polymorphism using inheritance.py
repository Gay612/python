class mother:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class father(mother):
    def var(self):
        print(self.name)
class son(mother):
    def var(self):
        print(self.name)
m=mother("maha")
f=father("govind")
s=son('mahe')
for i in(m, f,s):
    i.var()
