from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root=Tk()
root.title("Matplot GUI")
root.geometry('400x200')

def graph():
    house_prices =np.random.normal(200000,25000,5000)
    plt.polar(house_prices)
    #plt.title('Histogram')
    #plt.xlabel('House prices')
    #plt.ylabel('Datas')
    plt.show()

mybtn=Button(root,text='Graph It!',command=graph)
mybtn.pack()
root.mainloop()
