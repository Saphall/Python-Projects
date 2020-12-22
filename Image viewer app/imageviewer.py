from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title("CODE tk")

#Make the new image half the width and half the height of the original image
img1 = Image.open("Images/1.jpg")
image1 = img1.resize((round(img1.size[0]*0.5), round(img1.size[1]*0.5)))
img1=ImageTk.PhotoImage(image1)

img3 = Image.open("Images/3.jpg")
image3 = img3.resize((round(img3.size[0]*0.3), round(img3.size[1]*0.3)))
img3=ImageTk.PhotoImage(image3)
img4 = Image.open("Images/4.jpg")
image4 = img4.resize((round(img4.size[0]*0.4), round(img4.size[1]*0.4)))
img4=ImageTk.PhotoImage(image4)

image_list=[img1,img3,img4]

status = Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)


my_Label = Label(image=img1)
my_Label.grid(row=0,column=0,columnspan=3)

def forward (image_number):
    global my_Label
    global forward_button
    global back_button

    my_Label.grid_forget()
    my_Label=Label(image=image_list[image_number-1])
    forward_button = Button(root,text=">>",command=lambda:forward(image_number+1))
    back_button = Button(root,text="<<",command=lambda:backword(image_number-1))
    if image_number ==3:
        forward_button=Button(root,text=">>",state=DISABLED)

    back_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)
    my_Label.grid(row=0,column=0,columnspan=3)

    status = Label(root,text="Image "+ str(image_number) +" of "+str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)



def backword(image_number):
    global my_Label
    global forward_button
    global back_button

    my_Label.grid_forget()
    my_Label=Label(image=image_list[image_number-1])
    forward_button = Button(root,text=">>",command=lambda:forward(image_number+1))
    back_button = Button(root,text="<<",command=lambda:backword(image_number-1))
    if image_number ==1:
        back_button=Button(root,text="<<",state=DISABLED)

    back_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)
    my_Label.grid(row=0,column=0,columnspan=3)

    status = Label(root,text="Image "+ str(image_number) +" of "+str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)


back_button= Button(root,text="<<",command=backword,state=DISABLED)
back_button.grid(row=1,column=0)

forward_button = Button (root,text=">>",command=lambda:forward(2))
forward_button.grid(row=1,column=2,pady=10)

exit_button = Button(root,text="Exit Program",command = root.quit)
exit_button.grid(row=1,column=1)


root.mainloop()
