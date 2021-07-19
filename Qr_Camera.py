#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from pyzbar.pyzbar import decode
import cv2
import pyautogui
import numpy as np
from PIL import Image, ImageTk, ImageDraw
import os

class App:
    def __init__(self,font_video=0):
        self.active_camera = False
        self.info = []
        self.appName = 'QR Code Camera'
        self.ventana = Tk()
        self.ventana.title(self.appName)
        self.ventana['bg']='black'
        self.font_video=font_video
        self.label=Label(self.ventana,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        self.display=scrolledtext.ScrolledText(self.ventana,width=86,background='snow3'
                                        ,height=4,padx=10, pady=10,font=('Arial', 10))
        self.display.pack(side=BOTTOM)
        
        self.canvas=Canvas(self.ventana,bg='black',width=640,height=480)
        self.canvas.pack()
        self.btnLoad = Button(self.ventana,text="CARGAR ARCHIVO",width=29,bg='goldenrod2',
                    activebackground='red',command=self.abrir)
        self.btnLoad.pack(side=LEFT)
        self.btnCamera = Button(self.ventana,text="INICIAR CAPTURA POR CAMARA",width=29,bg='goldenrod2',
                                activebackground='red',command=self.active_cam)
        self.btnCamera.pack(side=LEFT)
        self.btnScreen = Button(self.ventana,text="DETECTAR EN PANTALLA",width=30,bg='goldenrod2',
                                activebackground='red',command=self.screen_shot)
        self.btnScreen.pack(side=LEFT)

        self.ventana.mainloop()
        
    def abrir(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",
                    filetypes =(("png files","*.png") ,("jpg files","*.jpg")))
        if ruta != "":
            archivo = cv2.imread(ruta)
            self.info = decode(archivo)
            if self.info != []:
                self.display.delete('1.0',END)
                self.display.insert(END,self.info[0][0])
            else:
                messagebox.showwarning("ERROR","NO SE DETECTÓ CÓDIGO")
        
    def screen_shot(self):
        pyautogui.screenshot("QRsearch_screenshoot.jpg")
        archivo = cv2.imread("QRsearch_screenshoot.jpg")
        self.info = decode(archivo)
        if self.info != []:
            self.display.delete('1.0',END)
            self.display.insert(END,self.info[0][0])
        else:
            messagebox.showwarning("QR NO ENCONTRADO","NO SE DETECTÓ CÓDIGO")
        os.remove("QRsearch_screenshoot.jpg")
        
    def visor(self):
        ret, frame=self.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)
            self.ventana.after(15,self.visor)
                    
    def active_cam(self):
        if self.active_camera == False:
            self.active_camera = True
            self.VideoCaptura()
            self.visor()
        else:
            self.active_camera = False
            self.btnCamera.configure(text="INICIAR CAPTURA POR CAMARA")
            self.vid.release()
            self.canvas.delete('all')
            #self.canvas.destroy()
            
    def capta(self,frm):
        self.info = decode(frm)
        if self.info != []:
            self.display.delete('1.0',END)
            self.display.insert(END,self.info[0][0])
            self.draw_rectangle(frm)

    def get_frame(self):
        if self.vid.isOpened():
            verif,frame=self.vid.read()
            if verif:
                self.btnCamera.configure(text="CERRAR CAMARA")
                self.capta(frame)
                return(verif,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                messagebox.showwarning("CAMARA NO DISPONIBLE","""La cámara está siendo utilizada por otra aplicación.
                Cierrela e intentelo de nuevo.""")
                self.active_camera = False
                return(verif,None)
        else:
            verif=False
            return(verif,None)
        
    def draw_rectangle(self,frm):
        codes = decode(frm)
        for code in codes:
            data = code.data.decode('ascii')
            x, y, w, h = code.rect.left, code.rect.top, \
                        code.rect.width, code.rect.height
            cv2.rectangle(frm, (x,y),(x+w, y+h),(255, 0, 0), 6)
            cv2.putText(frm, "QR Code", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)
            #cv2.rectangle(frm, code.polygon[0], code.polygon[1],
                          #(0, 255, 0), 4)
        
    def VideoCaptura(self):
        self.vid = cv2.VideoCapture(self.font_video)
        if self.vid.isOpened():
            self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.canvas.configure(width=self.width,height=self.height)
        else:
            messagebox.showwarning("CAMARA NO DISPONIBLE","El dispositivo no está activado o disponible")
            self.active_camera = False

    def __del__(self):
        if self.active_camera == True:
            self.vid.release()

if __name__=="__main__":
    App()
