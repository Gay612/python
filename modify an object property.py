class person:
    def __init__(self,fname,lname):
        self.a=fname
        self.b=lname
    def var(self):
        print(self.a,self.b)
p=person("gayu","maha")
p.lname='kavi'
print(p.lname)
p.var()
