from tkinter import *
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

        Entry(self.window,textvariable=self.currentDir,width=86).place(x=0,y=0)
        Label(self.window,text='ZZZZZZ...',bg='black',fg='green',font=('arial',20,'bold'),width=29).place(x=10,y=26)
        Button(self.window,text="CHANGE DIRECTORY",width=70).place(x=10,y=139)


        self.window.mainloop()

if __name__=="__main__":
    assistant()
