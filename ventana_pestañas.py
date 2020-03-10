#IMPORTAMOS "tkinter"
from tkinter import *
import tkinter
from tkinter import ttk

def saludo():
    print("Hola ",nombre.get())

def suma5():
    resultado=numero.get()+5
    print("RESULTADO: ",resultado)

def resta5():
    resultado=numero.get()-5
    print("RESULTADO: ",resultado)

def multi5():
    resultado=numero.get()*5
    print("RESULTADO: ",resultado)

def divid5():
    resultado=numero.get()/5
    print("RESULTADO: ",resultado)

#VENTANA PRINCIPAL.
root = tkinter.Tk()
root.title("VENTANA CON PESTAÑAS")
root.geometry("500x300")
nombre = StringVar()
numero = IntVar()

#INCLUIMOS PANEL PARA LAS PESTAÑAS.
nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

#CREAMOS PESTAÑAS
p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)
p5 = ttk.Frame(nb)

#ELEMENTOS PESTAÑA Saludo.
Button(p1, text='Saludar',bg='light blue',command=saludo).place(x=225,y=160)
Entry(p1, textvariable=nombre).place(x=190,y=70)
#ELEMENTOS PESTAÑA Suma5.
Button(p2, text='Suma5',bg='light blue',command=suma5).place(x=225,y=160)
Entry(p2, textvariable=numero).place(x=190,y=70)
#ELEMENTOS PESTAÑA Resta5.
Button(p3, text='Resta5',bg='light blue',command=resta5).place(x=225,y=160)
Entry(p3, textvariable=numero).place(x=190,y=70)
#ELEMENTOS PESTAÑA Multi5.
Button(p4, text='Multi5',bg='light blue',command=multi5).place(x=225,y=160)
Entry(p4, textvariable=numero).place(x=190,y=70)
#ELEMENTOS PESTAÑA Divid5.
Button(p5, text='Divid5',bg='light blue',command=divid5).place(x=225,y=160)
Entry(p5, textvariable=numero).place(x=190,y=70)

#AGREGAMOS PESTAÑAS CREADAS
nb.add(p1,text='Saludo')
nb.add(p2,text='Suma5')
nb.add(p3,text='Resta5')
nb.add(p4,text='Multi5')
nb.add(p5,text='Divid5')

root.mainloop()
