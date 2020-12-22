from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Driving License Verification")

img=Image.open("F:/Saphal/1-Programming/1python/2Python Projects/Image viewer app/Images/1.jpg")
im =img.resize((round(img.size[0]*0.5),round(img.size[1]*0.5)))
img=ImageTk.PhotoImage(im)

label = Label(image=img,width=500)
#label =Entry(root,bg="blue",width=100)
#label.insert(0,"Open a image")
label.grid(row=0,column=0,columnspan=2)

Capturebtn=Button(root,text="Capture/Open")
Capturebtn.grid(row=1,column=0)
Verifybtn=Button(root,text="Verify")
Verifybtn.grid(row=1,column=1)








root.mainloop()
