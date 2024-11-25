class name:
    name=" "
    def name(self):
        print(self.name)
class i_d:
    i_d=" "
    def i_d(self):
        print(self.i_d)
class age(name,i_d):
    age=" "
    def age(self):
        print(self.age)
    def student(self):
        print('name:',self.name)
        print('i_d:',self.i_d)
        print('age:',self.age)
x=age()
x.name='gayathri'
x.i_d=1234
x.age=17
x.student()
