from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as sct
from bs4 import BeautifulSoup
import threading
import os
import requests

class app():
    def __init__(self):
        self.root = Tk()
        self.root.title("GET HTML")
        self.root.geometry("900x600")
        self.root.configure(bg="gray70")
        self.html_display = sct.ScrolledText(self.root,width=105,height=27,bg="black",fg="white")
        self.html_display.place(x=20,y=37)

        self.url = StringVar()
        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        Entry(self.root,textvariable=self.currentDir,width=149).place(x=0,y=0)
        Entry(self.root,textvariable=self.url,width=50,font=('arial',14)).place(x=20,y=505)
        Button(self.root,text="GET HTML",width=89,bg="azure4",command=self.init_task).place(x=20,y=533)
        Button(self.root,text="COPY URL",width=9).place(x=580,y=505)
        
        
        self.root.mainloop()

    def init_task(self):
        t = threading.Thread(target=self.get_html)
        t.start()

    def get_html(self):
        try:
            web = self.url.get()
            result = requests.get(web)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            self.html_display.insert(END,soup.prettify())
        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))

if __name__=="__main__":
    app()
