from tkinter import *
from tkinter import filedialog
import cv2
import pyautogui
import threading
import os

class assistant:
    def __init__(self):
        self.window = Tk()
        self.window.title("Screen Assistant")
        self.window.geometry("520x250")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.awake = False

        Entry(self.window,textvariable=self.currentDir,width=86).place(x=0,y=0)
        self.statusLab = Label(self.window,text='ZZZZZZ...',bg='black',fg='green',font=('arial',20,'bold'),width=29)
        self.statusLab.place(x=10,y=26)
        self.btnActiv = Button(self.window,text="ACTIVATE",bg='blue',fg='white',width=70,height=3,command=self.wake_up)
        self.btnActiv.place(x=10,y=80)
        Button(self.window,text="CHANGE DIRECTORY",bg='khaki',width=70,height=3,command=self.change_dir).place(x=10,y=142)


        self.window.mainloop()

    def change_dir(self):
        new_dir = filedialog.askdirectory()
        if new_dir != "":
            os.chdir(new_dir)
            self.currentDir.set(os.getcwd())

    def wake_up(self):
        if self.awake == False:
            self.awake = True
            self.btnActiv.configure(text='ACTIVATED')
            self.statusLab.configure(text='NOW LISTENING...')
        else:
            self.awake = False
            self.btnActiv.configure(text='ACTIVATE')
            self.statusLab.configure(text='ZZZZZZ...')            
        

if __name__=="__main__":
    assistant()
