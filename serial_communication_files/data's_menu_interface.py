from tkinter import*
import time
import os
import matplotlib.pyplot as plt
import numpy as np

window= Tk()
window.title("___Serial_Communication_Data_Menu___")


def datas(event):
    
    text3=Label(window)
    text3.config(text="you will see datas")
    text3.pack()
    # time.sleep(2)

    with open('datas_storage_notebook.txt','r')as f:
        readed=f.read()
    window2=Tk()  
    text4= Label(window2)
    text4.config(text=readed)
    text4.pack()

#**************---------****************----------***********#
def data_graps(event):
    
    text5=Label(window)
    text5.config(text="you will see datas")
    text5.pack()
    # time.sleep(2)

    with open('datas_storage_notebook.txt','r')as f:
        readed= f.read()
    
    list_of_readed_file=readed.split()
    time=list_of_readed_file[0::2]
    voltage=list_of_readed_file[1::2]
 

    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.xticks(rotation=90)
    plt.plot(time,voltage,'o-g')
    plt.show()
 

text1= Label(window)
text1.config(text="Welcome   SCDM    Interface",font="cocogoose 20")
text1.pack()

buton= Button(window)
buton.config(text="Time & Value"+'\n'+"Data"+'\n'+"Menu",font="cocogoose 30 bold")
buton.bind('<Button>',datas)
buton.pack(padx=100, pady=100)


buton2= Button(window)
buton2.config(text="Data's"+'\n'+"Graph"+'\n'+"Menu",font="cocogoose 28 bold")
buton2.bind('<Button>',data_graps)
buton2.pack(padx=100, pady=100)

mainloop()