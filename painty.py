import turtle
import tkinter as tk

def forward():
    t.forward(100)

def back():
    t.pencolor("white")
    t.back(100)
    t.pencolor(col)

def left():
    t.left(90)


def right():
    t.right(90)


def colore(c):
    global col
    t.pencolor(c)
    col = c

def size(s):
    t.pensize(s)

def color_fondo(cl):
    t.screen.bgcolor(cl)

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 700, height = 700)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("black") # Red #ff0000
col = "black"

#BOTONES DE DIRECCION
tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)
#BOTONES PARA COLOR DE LINEA
tk.Button(master = root, bg = "blue", width=2, command = lambda:colore("blue")).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "red", width=2, command = lambda:colore("red") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "green", width=2, command = lambda:colore("green") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "yellow", width=2, command = lambda:colore("yellow") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "black", width=2, command = lambda:colore("black") ).pack(side = tk.RIGHT)
tk.Label(master = root, text = "COLOR").pack(side = tk.RIGHT)
#BOTONES PARA GROSOR DE LINEA
tk.Button(master = root, text = 1, width=2, command = lambda:size(1)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 3, width=2, command = lambda:size(3)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 5, width=2, command = lambda:size(5)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 7, width=2, command = lambda:size(7)).pack(side = tk.RIGHT)
tk.Button(master = root, text = 10, width=2, command = lambda:size(10)).pack(side = tk.RIGHT)
tk.Label(master = root, text = "GROSOR").pack(side = tk.RIGHT)
#BOTONES PARA COLOR DE FONDO
tk.Button(master = root, bg = "blue", width=2, command = lambda:color_fondo("blue")).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "red", width=2, command = lambda:color_fondo("red") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "green", width=2, command = lambda:color_fondo("green") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "yellow", width=2, command = lambda:color_fondo("yellow") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "black", width=2, command = lambda:color_fondo("black") ).pack(side = tk.RIGHT)
tk.Label(master = root, text = "COLOR FONDO").pack(side = tk.RIGHT)

root.mainloop()
