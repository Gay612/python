name=input('enter your name:')
location=input('enter your location:')
print(name,location)
f=open("C:/Users/admin/Desktop/gayathri/file.txt","w")
f.write(name)
f.write(location)
f.close()