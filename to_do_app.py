import os
import tkinter as tk
from tkinter import ttk, Tk

class ToDo:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("898x600")
        self.root.title("To Do List")

        current_dir = tk.StringVar()
        current_dir.set(os.getcwd())

        tk.Entry(self.root, textvariable=current_dir,width=149).place(x=0,y=0)

        


if __name__ == "__main__":
    ToDo()
