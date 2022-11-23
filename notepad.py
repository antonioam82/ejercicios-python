from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter as tk
import os

#FUNCIÓN PARA GUARDAR TEXTO EN ARCHIVO .TXT
def saveFile():
    if len(entry.get('1.0',END)) > 1:
        doc = asksaveasfilename(title="save text",
                                initialfile="my_text",
                                defaultextension=".txt")
        if doc != "":
            new_file = open(doc,"w")
            text = str(entry.get(1.0, END))
            new_file.write(text)
            new_file.close()

#FUNCIÓN PARA ABRIR Y LEER ARCHIVOS DE TEXTO
def openFile():
    file = askopenfile(mode = 'r', filetype =[('text_files', '*.txt')])
    if file is not None:
        if len(entry.get('1.0',END))>1:
            clearFile()                 #LLAMADA A FUNCIÓN 'clearFile()'
        content = file.read()
        entry.insert(INSERT, content)

#FUNCIÓN PARA LIMPIAR ÁREA DE TEXTO
def clearFile():
    entry.delete('1.0',END)

#FUNCIÓN PARA CERRAR VENTANA.
def destroy_window():
    if len(entry.get('1.0',END)) > 1:
        question = askquestion("GUARDAR?",
                               "¿Desea guardar los cambios hechos en el documento?")
        if question == "yes":
            saveFile()       #LLAMADA A FUNCIÓN "saveFile()"
        else:
            pass
    canvas.destroy()

#CREACIÓN VENTANA 
canvas = tk.Tk()
canvas.geometry("550x660")
canvas.title("Notepad")
canvas.config(bg = "white")

#SALIDA PARA DIRECTORIO ACTUAL
current_dir = StringVar()
current_dir.set(os.getcwd())
Entry(canvas,textvariable=current_dir).pack(padx=0,pady=0,fill="both")

#CONTENEDOR PARA LOS BOTONES
top = Frame(canvas)
top.pack(padx = 10, pady = 3, anchor = "nw")

#BOTONES
b1 = Button(canvas,text="Open",bg="white",command=openFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(canvas,text="Save",bg="white",command=saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(canvas,text="Clear",bg="white",command=clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(canvas,text="Exit",bg="white",command=destroy_window)
b4.pack(in_ = top, side=LEFT)

#ELEMENTO CANVAS PARA ENTRADA DE TEXTO Y BARRA DE SCROLL
canvas2 = Canvas(canvas)
canvas2.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

#BARRA DE SCROLL LATERAL
scrollbar = Scrollbar(canvas2,orient=VERTICAL)
scrollbar.pack(side = RIGHT, fill = Y)

#ENTRADA PARA TEXTO
entry = Text(canvas2, wrap = WORD, bg = "azure", font = ("poppins", 15))#wrap = WORD
entry.pack(side = LEFT, fill = BOTH, expand = TRUE)

#CONECTAR BARRA DE SCROLL Y ENTRADA
entry.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = entry.yview)

canvas.mainloop()
