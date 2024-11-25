from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
new_im=im.resize((800,600))
new_im.show()
