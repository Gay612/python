from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
r,g,b=im.split()
r.show()
g.show()
b.show()
c,y,k=im.split()
c.show()
y.show()
k.show()

#merging
new=Image.merge('RGB',(r,g,b))
new.show()
