class mark:
    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
class total(mark):
    def __init__(self,mark1,mark2,mark3):
        self.total=total
        mark.__init__(self,mark1,mark2,mark3)
        self.total=self.mark1+self.mark2+self.mark3
class average(total):
    def __init__(self,mark1,mark2,mark3):
        self.average=average
        total.__init__(self,mark1,mark2,mark3)
        self.average=self.total/3
    def dog(self):
        print(self.average)
        print(self.total)
a=average(98,97,97)
a.dog()
         
         
         
        
        
