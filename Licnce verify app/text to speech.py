from tkinter import *
from PIL import ImageTk, Image
from win32com.client import Dispatch

root=Tk()
root.title("Driving Licnece Verification")
img=ImageTk.PhotoImage(Image.open("Licence.jpg"))
label=Label(image=img)
label.grid(row=0,column=0,columnspan=2)


def speak():
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak("Driving Licence is valid ! Thank You!")
#if __name__ == '__main__':
#    speak("Driving License is verified ! Thank You!")

capture=Button(root,text="Capture/Open",borderwidth=10,bg="green",fg="white")
capture.grid(row=3,column=0)
verify = Button(root,text="Verify",width=10,borderwidth=10,bg="yellow",command=speak)
verify.grid(row=3,column=1)



root.mainloop()
