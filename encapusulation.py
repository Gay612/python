class parent:
    def __init__(self):
        self.a=2
class child:
    def __init__(self):
        parent.__init__(self)
        print(self.a)
        self.a=3
        print(self.a)
    
x=child()
y=parent()
print(x.a)
print(y.a)
