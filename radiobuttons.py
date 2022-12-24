from tkinter import *

#FUNCIÓN PARA MOSTRAR OPCIÓN SELECCIONADA
def select():
    outLabel.config(text = "Opción {}".format(option.get()))

#FUNCIÓN DE 'RESET'
def reset():
    option.set(None)
    outLabel.config(text="")

#CREAR VENTANA
root = Tk()
root.title("RADIOBUTTONS")
root.config(bd=90)

option = IntVar() #VARIABLE DE OPCIÓN

#CREAR RADIOBUTTONS
Radiobutton(root, text="Opción 1", variable=option, 
            value=1, activebackground="light gray",
            activeforeground="blue",command=select).pack()
Radiobutton(root, text="Opción 2", variable=option,
            value=2, activebackground="light gray",
            activeforeground="blue",command=select).pack()
Radiobutton(root, text="Opción 3", variable=option, 
            value=3, activebackground="light gray",
            activeforeground="blue",command=select).pack()

#ETIQUETA DE SALIDA
outLabel = Label(root)
outLabel.pack()

#BOTÓN DE 'RESET'
Button(root, text="RESET", command=reset).pack()


root.mainloop()
