from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter as tk

def saveFile():
    doc = asksaveasfilename(title="save text", initialfile="my_text",defaultextension=".txt")
    if doc != "":
        new_file = open(doc,"w")
        text = str(entry.get(1.0, END))
        new_file.write(text)
        new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype =[('text_files', '*.txt')])
    if file is not None:
        if len(entry.get('1.0',END))>1: ###############
            clearFile()
        content = file.read()
        entry.insert(INSERT, content)

def destroy_window():
    if len(entry.get('1.0',END)) > 1:
        question = askquestion("GUARDAR?","¿Desea guardar los cambios hechos en el documento?")
        if question == "yes":
            saveFile()
        else:
            pass
    canvas.destroy()

def clearFile():
    entry.delete('1.0',END)

canvas = tk.Tk()
canvas.geometry("780x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = "nw")

b1 = Button(canvas,text="Open",bg="white", command=openFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(canvas,text="Save",bg="white", command=saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(canvas,text="Clear",bg="white",command=clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(canvas,text="Exit",bg="white", command=destroy_window)
b4.pack(in_ = top, side=LEFT)

entry = Text(canvas, wrap = WORD, bg = "azure", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

canvas.mainloop()
