from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
flip=im.transpose(Image.ROTATE_180)
flip.show()
