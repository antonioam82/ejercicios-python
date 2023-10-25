#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import ttk, Tk, Listbox, Canvas
import json

class ToDo:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("898x600")
        self.root.title("To Do List")

        current_dir = tk.StringVar()
        current_dir.set(os.getcwd())

        tk.Entry(self.root, textvariable=current_dir,width=149).place(x=0,y=0)
        self.canvas = Canvas(self.root,bg="blue")#,width=500,height=500)
        self.canvas.place(x=9,y=27)
        self.todo_list = Listbox(self.canvas,bg="gray96",width=80,height=30)
        self.todo_list.pack()
        


if __name__ == "__main__":
    ToDo()


