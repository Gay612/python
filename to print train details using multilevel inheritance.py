class train:
    def __init__(self,number):
        self.number = number
    def display_train_details(self):
        print(self.number)
class coach(train):
    def __init__(self,number,coach):
        super().__init__(number)
        self.coach=coach
    def display_coach_details(self):
        print(self.coach)
class passenger(coach):
    def __init__(self,number,coach,seat,name,age):
      super().__init__(number,coach)
      self.seat=seat
      self.name=name
      self.age=age
    def  display_passenger_details(self):
        print(self.seat)
        print(self.name)
        print(self.age)
number=input('enter a train number:')
coach=input('enter a coach number:')
seat=input('enter a seat number:')
name=input('enter passenger name:')
age=input('enter passenger age:')
p=passenger(number,coach,seat,name,age)
print('\n train details:')
p.display_passenger_details()
p.display_coach_details()
p.display_train_details()
