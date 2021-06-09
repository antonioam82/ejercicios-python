from tkinter import *
import cv2
import pyautogui
import threading
import os

class assistant:
    def __init__(self):
        self.window = Tk()
        self.window.title("Screen Assistant")
        self.window.geometry("500x250")


        self.window.mainloop()

if __name__=="__main__":
    assistant()
