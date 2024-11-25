with open("C:/Users/admin/Desktop/gayathri/file.txt","r")as f1,open("C:/Users/admin/Desktop/gayathri/file2.txt","a")as f2:
    for i in f1:
        print(i)
        f2.write(i)
