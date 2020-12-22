from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import pytesseract
from win32com.client import Dispatch


root = Tk()
root.title("Driving Licence Verification App")
#root.geometry('800x500')

frame = LabelFrame(root,text='License Image here',padx=20,pady=20,font=1)
frame.grid(row=0,column=0,padx=10,pady=10)
img=ImageTk.PhotoImage(Image.open("download.png"))
label=Label(frame,image=img)
label.grid(row=0,column=0)

# FUNCTIONS
def text_detection(loc):
    #img=Image.open(loc)
    #custom_config = ' --oem 3 --psm 6'
    #extractedText = pytesseract.image_to_string(img, lang='eng',config=custom_config)
    print(loc)


def open():
    root.filename=filedialog.askopenfilename(initialdir='2Licnce verify app',title='Select Driving License',filetypes=(('jpeg','*.jpg'),('png files','*.png')))
    #label = Label(frame,text=root.filename).grid(row=0,column=0)
    try:
        global img
        img=ImageTk.PhotoImage(Image.open(root.filename))
        label=Label(frame,image=img).grid(row=0,column=0)
        text_detection(root.filename)
    except:
        print('No Image selected')



frame2=Frame(root,bg='light blue')
frame2.grid(row=0,column=1)
b1=Button(frame2,text='Capture/Open',command=open,width=20,borderwidth=3,bg='cyan')
b1.grid(row=0,column=0,padx=20,pady=10)
b2=Button(frame2,text='Verify',width=20,borderwidth=3,bg='light green')
b2.grid(row=1,column=0,padx=20,pady=10)

root.mainloop()
