from datetime import datetime
class person:
    def __init__(self,name,country,stdno,dob):
        self.name=name
        self.country=country
        self.std=stdno
        self.dob=datetime.strptime(dob,'%Y-%m-%d')
    def calc(self):
        today=datetime.today()
        age=today.year - self.dob.year
        return age
    def var(self):
        print(self.name)
        print(self.country)
        print(self.std)
        print(self.dob)
p=person('gayathri','India',1234,'2006-09-18')
p.var()
print(p.calc())
         
