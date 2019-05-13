import turtle
import tkinter as tk
from tkinter import colorchooser

#FUNCIONES DE MOVIMIENTO.
def mover():
    t.forward(100)

def atras():
    t.back(100)

def izq():
    t.left(90)

def der():
    t.right(90)

#FUNCIONES DE COLOR.
    
def color_fondo():
    cl = colorchooser.askcolor()
    if cl != (None, None):
        co = list(cl)
        t.screen.bgcolor(co[1])

def color():
    cl = colorchooser.askcolor()
    if cl != (None, None):
        co = list(cl)
        t.pencolor(co[1])


#FUNCION PARA GROSOR DE LINEA.

def grosor(n):
    t.pensize(n)
    
    
root = tk.Tk()
root.title("Painty")
canvas = tk.Canvas(master = root, width = 700, height = 700)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("black")

#BOTONES DE DIRECCION.
tk.Button(master = root, text = "Mover", command = mover).pack(side = tk.LEFT)
tk.Button(master = root, text = "Atras", command = atras).pack(side = tk.LEFT)
tk.Button(master = root, text = "Izquierda", command = izq).pack(side = tk.LEFT)
tk.Button(master = root, text = "Derecha", command = der).pack(side = tk.LEFT)

#BOTONES PARA ELECCION DE COL0R.
tk.Button(master = root, text = "COLOR PINCEL", command = color).pack(side = tk.RIGHT)
tk.Button(master = root, text = "COLOR FONDO", command = color_fondo).pack(side = tk.RIGHT)

#BOTONES PARA GROSOR DE LINEA
tk.Button(master = root, text = 1, width=2, command = lambda:grosor(1)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 3, width=2, command = lambda:grosor(3)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 5, width=2, command = lambda:grosor(5)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 7, width=2, command = lambda:grosor(7)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 10, width=2, command = lambda:grosor(10)).pack(side = tk.RIGHT)
tk.Label(master = root, text = "GROSOR").pack(side = tk.RIGHT)

root.mainloop()
