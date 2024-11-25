import pickle
a=open("C:/Users/admin/Desktop/student.dat","br")
b=list(pickle.load(a))
print(b)
a.close()
