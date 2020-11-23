from tkinter import *
from tkinter import messagebox
import cv2
from mhmovie.code import *
import numpy as np
from PIL import Image, ImageTk
import threading
import time
import os
import glob

if not os.path.exists(os.getcwd()+"\CAMARA_VIDEOS"):
    os.makedirs("CAMARA_VIDEOS")
os.chdir(os.getcwd()+"\CAMARA_VIDEOS")

def future_file():
    name = "output.avi"
    count = 0
    for i in glob.glob('*.avi'):
        if "output" in i:
            count+=1
    if count>0:
        name = "output"+"("+str(count)+")"+".avi"
    return name

class App:
    def __init__(self,font_video=0):
        global name_file
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        name_file = future_file()
        self.hours = 0
        self.minuts = 0
        self.seconds = 0
        self.out = cv2.VideoWriter(name_file,self.fourcc, 20.0, (640,480))
        self.appName = "camera"
        self.ventana = Tk()
        self.ventana.title(self.appName)
        self.ventana['bg']='black'
        self.font_video=font_video
        self.recording=False
        self.vid=VideoCaptura(self.font_video)#!!!!!!!!!!!!!!!!!!!!!!!!!
        self.label=Label(self.ventana,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        
        self.canvas=Canvas(self.ventana,bg='red',width=self.vid.width,height=self.vid.height)
        self.canvas.pack()
        self.btnScreenshot = Button(self.ventana,text="Photo",width=28,bg='goldenrod2',
                    activebackground='red',command=self.captura)
        self.btnRecord = Button(self.ventana,text='Record',width=29,bg='red',
                                fg='white',command=self.record)
        self.btnRecord.pack(side=LEFT)        
        self.btnScreenshot.pack(side=RIGHT)
        self.counter = Label(self.ventana,text='00:00:00',bg='black',fg='red',width=27,height=2,font=('Arial',11))#27
        self.counter.pack(side=LEFT)        


        self.visor()
        self.ventana.mainloop()

    #def show_photo_name(self):
        #self.counter.config(text=self.image)
        #time.sleep(2)
        #self.counter.config(text='00:00:00')

    #def init_name(self):
        #t2 = threading.Thread(target=self.show_photo_name)
        #t2.start()
        
    def captura(self):
        ver,frame=self.vid.get_frame()
        if ver:
            image="IMG-"+time.strftime("%H-%M-%S-%d-%m")+".jpg"
            cv2.imwrite(image,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            self.counter.config(text=image)
            #self.init_name()
            
    def visor(self):
        ret, frame=self.vid.get_frame()
        flip = cv2.flip(frame,1)##########################################
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(flip))#frame
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)#0,0
            if self.recording == True:
                frame = cv2.cvtColor(flip, cv2.COLOR_BGR2RGB)#frame
                self.out.write(flip)#frame
            self.ventana.after(15,self.visor)

    def record(self):
        global name_file
        if self.recording == False:
            self.recording = True
            self.clear_timer()
            self.init_timer()
            self.btnRecord.configure(text='Stop')
            
        else:
            self.recording = False
            self.btnRecord.configure(text='Record')
            self.counter.after_cancel(self.process)
            name_file = future_file()
            self.out = cv2.VideoWriter(name_file,self.fourcc, 20.0, (640,480))
            #VideoCaptura()

    def formato(self,c):
        if c<10:
            c="0"+str(c)
        return c

    def clear_timer(self):
        self.hours=0
        self.minuts=0
        self.seconds=0
        
    def cuenta(self):
        self.counter['text'] = str(self.formato(self.hours))+":"+str(self.formato(self.minuts))+":"+str(self.formato(self.seconds))
        
        if self.seconds==60:
            self.seconds=0
            self.minuts+=1
        if self.minuts==60:
            self.minuts=0
            self.hours+=1
        self.seconds+=1
        self.process=self.counter.after(1000,self.cuenta)

    def init_timer(self):
        t = threading.Thread(target=self.cuenta)
        t.start()
        
class VideoCaptura:
    def __init__(self,font_video=0):
        self.vid = cv2.VideoCapture(font_video)
        if not self.vid.isOpened():
            raise ValueError("No se puede usar esta camara")
        self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def get_frame(self):
        if self.vid.isOpened():
            verif,frame=self.vid.read()
            inverted=cv2.flip(frame,0)#####################################
            if verif:
                return(verif,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))#verif
            else:
                return(verif,None)
        else:
            return(verif,None)
        

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            os.remove(name_file)
        print("OK")

if __name__=="__main__":
    App()
