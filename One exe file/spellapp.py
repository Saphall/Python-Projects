from tkinter import *
from win32com.client import Dispatch

root=Tk()
root.title("Spell App")
#root.geometry('340x100')

def speak(e):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(e)
#if __name__ == '__main__':
#    speak("Driving License is verified ! Thank You!")

e=Entry(root,width=50)
e.grid(row=0,column=1,pady=(20,0),padx=10)
spell = Button(root,text="Spell",width=10,bg="yellow",command=lambda:speak(e.get()))
spell.grid(row=1,column=1,pady=10,columnspan=2)



root.mainloop()
