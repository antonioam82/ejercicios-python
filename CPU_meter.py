#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import psutil

def cpu_met():
    cpu_use = psutil.cpu_percent(interval = 1)
    cpu_label.config(text='{}%'.format(cpu_use))
    cpu_label.after(200,cpu_met)

ventana = Tk()
ventana.geometry("480x140")
ventana.title("Total CPU Usage")
ventana.configure(bg='midnight blue')
cpu_label = Label(ventana,bg="black",fg="green",anchor=NE,font="Arial 30 bold",width=6)
cpu_label.place(x=230,y=20)

digi=Label(ventana,text="CPU Usage:",font="arial 24 bold",bg='midnight blue',fg="white")
digi.place(x=20,y=25)

cpu_met()

ventana.mainloop()

