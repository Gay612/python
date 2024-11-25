class person:
    def __init__(self,name):
        self.name=name
    def abc(self):
        print(self.name)
class stu(person):
   def __init__(self,name):
       person.__init__(self,name)
x=stu('gayu') 
x.abc()

