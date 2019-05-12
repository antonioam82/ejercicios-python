import turtle
import tkinter as tk

#FUNCIONES DE MOVIMIENTO.
def mover():
    t.forward(100)

def atras():
    t.back(100)

def izq():
    t.left(60)

def der():
    t.right(60)

#FUNCIONES DE COLOR.

def color_linea(c):
    t.pencolor(c)

def color_fondo(c):
    t.screen.bgcolor(c)

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

#BOTONES PARA COLOR DE LINEA.
tk.Button(master = root, bg = "blue", width=2, command = lambda:color_linea("blue")).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "red", width=2, command = lambda:color_linea("red") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "green", width=2, command = lambda:color_linea("green") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "yellow", width=2, command = lambda:color_linea("yellow") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "black", width=2, command = lambda:color_linea("black") ).pack(side = tk.RIGHT)
tk.Label(master = root, text = "COLOR").pack(side = tk.RIGHT)

#BOTONES PARA COLOR DE FONDO.
tk.Button(master = root, bg = "blue", width=2, command = lambda:color_fondo("blue")).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "red", width=2, command = lambda:color_fondo("red") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "green", width=2, command = lambda:color_fondo("green") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "yellow", width=2, command = lambda:color_fondo("yellow") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "black", width=2, command = lambda:color_fondo("black") ).pack(side = tk.RIGHT)
tk.Label(master = root, text = "COLOR FONDO").pack(side = tk.RIGHT)

#BOTONES PARA GROSOR DE LINEA
tk.Button(master = root, text = 1, width=2, command = lambda:grosor(1)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 3, width=2, command = lambda:grosor(3)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 5, width=2, command = lambda:grosor(5)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 7, width=2, command = lambda:grosor(7)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 10, width=2, command = lambda:grosor(10)).pack(side = tk.RIGHT)
tk.Label(master = root, text = "GROSOR").pack(side = tk.RIGHT)

root.mainloop()
