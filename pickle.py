import pickle
a=open("C:/Users/admin/Desktop/student.dat","bw")
b=[17,"gayu",2006]
pickle.dump(b,a)
a.close()
