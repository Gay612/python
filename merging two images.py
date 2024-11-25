from PIL import  Image
im=Image.open("c:/archana/download.jpg")
im.show()
new=Image.open("c:/archana/download.jpg  ")
new.show()
position((im.width-new.width),(im.height-new.height))
im.paste(new,position)
im.show()
