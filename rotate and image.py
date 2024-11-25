from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
rot=im.rotate(45)
rot.show()
