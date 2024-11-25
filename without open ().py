a=["C:/Users/admin/Desktop/gayathri/file.txt","C:/Users/admin/Desktop/gayathri/file.txt"]
f1=open("C:/Users/admin/Desktop/gayathri/file3.txt","w")
for  i in  a:
       f2=open(i)
       f1.write(f2.read())
f1.close()
