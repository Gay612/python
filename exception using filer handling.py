try:
    f=open("C:/Users/admin/Desktop/gayathri/txt.text")
    try:
     f.write("heloo")
    except:
     print("can't write")
    finally:
     f.close()
except:
    print("can't open")
