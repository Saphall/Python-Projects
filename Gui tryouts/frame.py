from tkinter import *

root =Tk()
root.title("Frames")

#frame = LabelFrame(root,text="This is Frame",padx=50,pady=50)
#frame.pack(padx=10,pady=10)

#b=Button(frame,text="Click")
#b.pack()

#r = IntVar()
#r.set("1")

MODES =[
    ("Mushroom","Mushroom "),
    ("Cheese","Cheese"),
    ("Onion","Onion"),
]
pizz=StringVar()
pizz.set("Mushroom")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizz,value=mode,command=lambda : clicked(pizz.get())).pack(anchor=W)


def clicked(value):
    label= Label(root,text=value)
    label.pack()

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()

label= Label(root,text=pizz.get())
label.pack()



root.mainloop()
