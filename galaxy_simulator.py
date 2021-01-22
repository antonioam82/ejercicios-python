import tkinter as tk
from random import randint,uniform,random
import math

SCALE = 255
NUM_CIVS = 15600000

root = tk.Tk()
root.title("Milky Way Galaxy")
c = tk.Canvas(root,width=1000,height=800,bg="black")
c.grid()
c.configure(scrollregion=(-500,-400,500,400))

root.mainloop()

