from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
im.thumbnail((800,600))
im.show()
