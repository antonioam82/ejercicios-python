from tkinter import *
from locale import getdefaultlocale
from tkinter import messagebox,filedialog
from tkinter import ttk
import string
import random
import threading
import pyperclip
import os
import sys
#import time

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("PASSWORD GENERATOR")
        self.activated = True
        self.root.geometry("899x290")
        self.numbs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
                      25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,
                      47,48,49,50]
        
        self.your_password = StringVar()
        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.running = False
        lang = getdefaultlocale()[0]
        if 'es_' in lang:
            self.special_chars = "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}¬~€!ñÑ"
        else:
            self.special_chars = "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}¬~€!"

        Entry(self.root,textvariable=self.currentDir,width=149).place(x=0,y=0)
        Label(self.root,text="YOUR PASSWORD").place(x=10,y=30)
        Entry(self.root,textvariable=self.your_password,font=('arial 20'),width=58).place(x=10,y=50)
        Label(self.root,text="LENGTH:").place(x=10,y=110)
        self.stateLabel = Label(self.root,text="",width=127)
        self.stateLabel.place(x=2,y=141)
        self.btnCreate = Button(self.root,text="CREATE PASSWORD",width=123,height=2,bg="gray86",command=self.init_task)
        self.btnCreate.place(x=12,y=168)
        Button(self.root,text="SAVE PASSWORD",width=60,height=2,bg="gray86",command=self.save_password).place(x=12,y=218)
        Button(self.root,text="COPY",width=60,height=2,bg="gray86",command=self.copy).place(x=453,y=218)
        self.len=ttk.Combobox(self.root,width=5,state="readonly")
        self.len.place(x=68,y=110)
        Label(self.root,text="MIN LOWERCASE:").place(x=148,y=110)
        self.min_low=ttk.Combobox(self.root,width=5,state="readonly")
        self.min_low.place(x=255,y=110)
        Label(self.root,text="MIN UPPERCASE:").place(x=340,y=110)
        self.min_upp=ttk.Combobox(self.root,width=5,state="readonly")
        self.min_upp.place(x=440,y=110)
        Label(self.root,text="MIN NUMBERS:").place(x=525,y=110)
        self.min_num=ttk.Combobox(self.root,width=5,state="readonly")
        self.min_num.place(x=620,y=110)
        Label(self.root,text="MIN SPECIAL CHARS:").place(x=705,y=110)
        self.min_char=ttk.Combobox(self.root,width=5,state="readonly")
        self.min_char.place(x=831,y=110)
        self.len["values"]=self.numbs
        self.len.set(8)
        self.min_low["values"]=self.numbs
        self.min_low.set(0)
        self.min_upp["values"]=self.numbs
        self.min_upp.set(0)
        self.min_num["values"]=self.numbs
        self.min_num.set(0)
        self.min_char["values"]=self.numbs
        self.min_char.set(0)

        self.root.mainloop()

    def genera_password(self):
        #DEFINICIÓN DE LONGITUDES
        p_len = int(self.len.get())
        min_low = int(self.min_low.get())
        min_upp = int(self.min_upp.get())
        min_num = int(self.min_num.get())
        min_chars = int(self.min_char.get())

        #CARACTERES A USAR.
        characts = ''
        pos = 0
        liats = [string.digits,string.ascii_lowercase,string.ascii_uppercase,self.special_chars]
        sumas = [min_num,min_low,min_upp,min_chars]
        s = sum(sumas)
        if s == p_len and 0 in sumas:
            for i in sumas:
                if i != 0:
                    characts = characts+liats[pos]
                    print(characts)
                pos+=1
        else:
            characts = string.ascii_letters+string.digits+self.special_chars

        #BUSQUEDA/GENERACIÓN DE CONTRASEÑA
        self.stateLabel.configure(text="LOOKING FOR YOUR PASSWORD...",fg="red")
        while self.activated == True:
            pswrd=("").join(random.choice(characts) for i in range(p_len))
            self.your_password.set(pswrd)
            if(sum(c.islower() for c in pswrd)>=min_low
                and sum(c.isupper() for c in pswrd)>=min_upp
                and sum(c.isdigit() for c in pswrd)>=min_num
                and sum(c in self.special_chars for c in pswrd)>=min_chars):
                self.activated = False
                self.running = False

        #FIN DE TAREA       
        self.stateLabel.configure(text="TASK COMPLETED.",fg="blue")     
        if self.activated == False:
            self.btnCreate.configure(text="CREATE PASSWORD",command=self.init_task)
        self.your_password.set(pswrd)
        self.activated = True

    def copy(self):
        if self.your_password.get() != "" and self.running == False:
            pyperclip.copy(self.your_password.get())
            messagebox.showinfo("COPIED","Copied to clipboard.")
            
    def save_password(self):
        if len(self.your_password.get())>0 and self.running == False:
            question = messagebox.askquestion("ARE YOU SURE?",'''Saving password in plain texts is not a recommended practice.
Anyway, do you want to continue?''')
            if question == "yes":
                doc = filedialog.asksaveasfilename(initialdir="/",title="Save as",defaultextension='.txt')
                if doc != "":
                    document = open(doc,"w",encoding="utf-8")
                    document.write(str(self.your_password.get()))
                    document.close()
                    messagebox.showinfo("SAVED","Password saved correctly.")

    def cancel_process(self):
        self.activated = False
        self.running = False
        messagebox.showinfo("CANCELLED","Process cancelled.")

    def init_task(self):
        self.running = True
        if int(self.min_low.get()) + int(self.min_upp.get()) + int(self.min_num.get()) + int(self.min_char.get())<= int(self.len.get()):
            self.btnCreate.configure(text="CANCEL PROCESS",command=self.cancel_process)
            t = threading.Thread(target=self.genera_password)
            t.start()
        else:
            messagebox.showwarning("ERROR","INVALID LENGHT.")

if __name__=="__main__":
    app()
