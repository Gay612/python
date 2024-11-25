class person:
    def  __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class stu(person):
    pass
x=stu('gayu')
x.var()
