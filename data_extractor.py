from tkinter import *
import tkinter.scrolledtext as scrolledtext
from PIL import Image
from PIL.ExifTags import TAGS

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("DATA EXTRACTOR")
        #self.ventana.geometry("630x200")

        self.canvas = Canvas(self.ventana,bg='black',width=200,height=100)
        self.canvas.pack()
        
        self.ventana.mainloop()

if __name__=="__main__":
    App()
