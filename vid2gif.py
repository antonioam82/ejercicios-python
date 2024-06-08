import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
import threading
from PIL import Image, ImageTk

class GIFMaker(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('GIF Maker')
        self.geometry('800x850')

        self.video_path = ''
        self.output_path = ''
        self.frames = []
        self.preview_frame_index = 0

        self.select_video_button = tk.Button(self, text='Select Video',command=self.select_video) )
        self.select_video_button.pack(paddy=10)

        self.preview_label = tk.Label(self, text='Video Preview')
        self.preview_label.pack(paddy=10)

    def select_video(self):
        pass
