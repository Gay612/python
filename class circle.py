class circle:
   def __init__(self,radius):
        self.radius =radius
   def var(self):
        print('radius of circle=',3.14*self.radius**2)
radius=int(input('enter a number:'))           
a=circle(radius)
a.var()
