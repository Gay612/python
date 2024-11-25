class student:
    def __init__(self,name,i_d,mark1,mark2,mark3):
        self.name=name
        self.i_d=i_d
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def var(self):
        print(self.name,self.i_d,self.mark1,self.mark2,self.mark3)
        self.total=self.mark1+self.mark2+self.mark3
        self.average=self.total/3
    def abc(self):
        print(self.total)
        print(self.average)
p=student("gayu",1234,90,98,97)
p.var()
p.abc()
