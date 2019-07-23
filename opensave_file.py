#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import *
import os

ventana = Tk()

def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("jpeg files","*.jpg"),
                ("all files","*.*")))
    print(archivo_abierto)


def guardar_archivo():
    archivo_guardado=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",defaultextension=".txt",
                                 filetypes = (("jpeg files","*.jp2g"),
                                              ("txt files","*.txt"),
                                              ("all files","*.*")))
    
    archivo=open(archivo_guardado,"w")
    print(archivo_guardado)

def carpeta():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)
    print(os.getcwd())

Button(text="Abrir archivo",bg="pale green",command=abrir_archivo).place(x=10,y=10)
Button(text="Guardar archivo",bg="light blue",command=guardar_archivo).place(x=10,y=40)
Button(text="Directorio",bg="salmon",command=carpeta).place(x=10,y=70)

ventana.mainloop()
