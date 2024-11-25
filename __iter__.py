class num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
n=num()
b=iter(n)
for i in b:
    if i<=100:
        print(i)
    

