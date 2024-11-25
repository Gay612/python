

class mother:
    mothername=" "
    def mother(self):
        print(self.mothername)
class father:
    fathername=" "
    def father(self):
        print(self.fathername)
class son(mother,father):
    def parents(self):
        print("mother:",self.mothername)
        print("father:",self.fathername)
x=son()
x.mothername='maha'
x.fathername='govind'
x.parents()

        
