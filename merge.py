a=["C:/Users/admin/Desktop/gayathri/file.txt","C:/Users/admin/Desktop/gayathri/file2.txt"]
with open("C:/Users/admin/Desktop/gayathri/file3.txt","w")as f1:
    for i in a:
        with open(i) as f2:
         f1.write(f2.read())
