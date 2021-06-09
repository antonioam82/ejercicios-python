from tkinter import *
import cv2
import pyautogui
import threading
import os

class assistant:
    def __init__(self):
        self.window = Tk()
        self.window.title("Screen Assistant")
        self.window.geometry("515x250")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        Entry(self.window,textvariable=self.currentDir,width=85).place(x=0,y=0)



        self.window.mainloop()

if __name__=="__main__":
    assistant()
