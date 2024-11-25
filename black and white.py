from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
color=im.convert('1')
color.show()
