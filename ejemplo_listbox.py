#IMPORTAMOS TKINTER
from tkinter import *

#FUNCIÓN PARA AÑADIR ELEMENTOS.
def añadir():
    lista_elementos.insert(END, entrada.get())

    
#CREAMOS VENTANA
ventana=Tk()
ventana.geometry("700x600")
ventana.title("Lista")

#CREAMOS LISTBOX
lista_elementos=Listbox(ventana,width=50)

#AÑADIMOS ELEMENTOS
lista_elementos.insert(0,"Elemento 1")
lista_elementos.insert(1,"Elemento 2")
lista_elementos.insert(2,"Elemento 3")
lista_elementos.insert(3,"Elemento 4")

#UBICAMOS LA LISTA
lista_elementos.place(x=100,y=120)
lista_etiq=Label(ventana,text="Lista de Elementos").place(x=100,y=100)

#ENTRADA NUEVOS ELEMENTOS
entrada=StringVar()
entrada_elementos=Entry(ventana,textvariable=entrada,width=40).place(x=150,y=20)

#BOTON DE AÑADIR ELEMENTOS
boton_añadir=Button(ventana,text="añadir",heigh=2,width=18,command=añadir).place(x=400,y=20)

ventana.mainloop()
