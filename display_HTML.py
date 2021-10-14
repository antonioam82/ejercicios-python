from tkinter import *
import tkinter.scrolledtext as sct
from bs4 import BeautifulSoup
import os
import requests

class app():
    def __init__(self):
        self.root = Tk()
        self.root.title("GET HTML")
        self.root.geometry("900x600")
        self.root.configure(bg="gray70")
        self.html_display = sct.ScrolledText(self.root,width=105,height=27,bg="black",fg="white")
        self.html_display.place(x=20,y=30)

        self.url = StringVar()
        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        Entry(self.root,textvariable=self.currentDir,width=149).place(x=0,y=0)
        Entry(self.root,textvariable=self.url,width=70).place(x=20,y=490)
        
        
        self.root.mainloop()

if __name__=="__main__":
    app()
