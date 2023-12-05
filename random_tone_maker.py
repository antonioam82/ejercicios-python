#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth
from pydub.playback import play
import tkinter as tk
from tkinter import Tk, filedialog, messagebox, ttk
import os
import threading

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tone maker")
        self.root.geometry("700x500")
        self.root.resizable(height=False,width=False)

        self.root.mainloop()

if __name__ == "__main__":
    App()
