#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pyperclip
import time
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

        Label(self.root,text="URL",bg="gray70").place(x=20,y=487)
        Entry(self.root,textvariable=self.currentDir,width=149).place(x=0,y=0)
        Entry(self.root,textvariable=self.url,width=50,font=('arial',14)).place(x=20,y=505)
        Button(self.root,text="GET HTML",width=89,bg="azure4",command=self.init_task).place(x=20,y=533)
        Button(self.root,text="COPY URL",width=9,command=self.init_copy).place(x=580,y=505)
        Button(self.root,text="CLEAR",width=13,height=3,command=self.clear_display).place(x=669,y=505)
        Button(self.root,text="SAVE",width=13,height=3,command=self.save_html).place(x=781,y=505)
        
        
        self.root.mainloop()

    def copy_paste(self):
        messagebox.showinfo("COPY URL","Copy the URL you want.")
        self.ultima_copia = pyperclip.paste().strip()
        while True:
            time.sleep(0.1)
            self.copia = pyperclip.paste().strip()
            if self.copia != self.ultima_copia:
                self.url.set(self.copia)
                self.ultima_copia = self.copia
                break

    def is_url(self,url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def save_html(self):
        if len(self.html_display.get('1.0',END))>1:
               document = filedialog.asksaveasfilename(initialdir="/",
                          title="SAVE AS",initialfile="html",defaultextension=".txt")
               if document != "":
                   new_file = open(document,"w",encoding="utf-8")
                   lines = "URL: {}\n\n".format(self.web)
                   for l in str(self.html_display.get("1.0",END)):
                       lines=lines+l
                   new_file.write(lines)
                   new_file.close()
                   messagebox.showinfo("SAVED","HTML saved correctly.")

    def clear_display(self):
        self.html_display.delete('1.0',END)

    def BMP(self,s):
        return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

    def init_copy(self):
        t2 = threading.Thread(target=self.copy_paste)
        t2.start()

    def init_task(self):
        t = threading.Thread(target=self.get_html)
        t.start()

    def get_html(self):
        if self.url.get()!="":
            try:
                self.clear_display()
                is_url = self.is_url(self.url.get())
                if is_url:
                    self.web = self.url.get()
                    result = requests.get(self.web)
                    content =   self.BMP(result.text)
                    soup = BeautifulSoup(content, 'lxml')
                    self.html_display.insert(END,soup.prettify())
                else:
                    messagebox.showwarning("Invalid URL","Enter a valid URL")
                    self.url.set("")
            except Exception as e:
                messagebox.showwarning("CAN NOT GET HTML",str(e))
        else:
            messagebox.showwarning("NO URL","No URL provided")

if __name__=="__main__":
    app()

