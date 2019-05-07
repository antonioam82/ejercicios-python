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
    #t.forward(100)

def right():
    t.right(90)
    #t.forward(100)

def colore(c):
    global col
    t.pencolor(c)
    col = c

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 600, height = 600)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("black") # Red #ff0000
col = "black"
t.penup()   # Regarding one of the comments
t.pendown() # Regarding one of the comments

tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)
tk.Button(master = root, bg = "blue", command = lambda:colore("blue") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "red", command = lambda:colore("red") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "green", command = lambda:colore("green") ).pack(side = tk.RIGHT)
tk.Button(master = root, bg = "black", command = lambda:colore("black") ).pack(side = tk.RIGHT)
root.mainloop()
