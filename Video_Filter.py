from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import cv2 as cv
import ffmpeg
import numpy as np
import threading
from pydub import AudioSegment
import os
 
class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Video Filter")
        self.root.geometry("905x246")
        self.root.configure(bg="lavender")
 
        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.filename = StringVar()
        self.file = None
        self.canceled = False
        self.frames_list = []
        self.vid_name = None
        #self.question = "yes"
 
        Entry(self.root,textvariable=self.currentDir,width=158).place(x=0,y=0)
        Entry(self.root,textvariable=self.filename,font=('arial',23,'bold'),width=40).place(x=10,y=25)
        self.btnSearch = Button(self.root,text="SEARCH",height=2,width=25,bg="light blue1",command=self.open_file)
        self.btnSearch.place(x=709,y=25)
        self.btnStart = Button(self.root,text="START FILTERING",width=97,height=2,bg="light green",command=self.init_task)
        self.btnStart.place(x=8,y=77)
        Button(self.root,text="CANCEL",height=2,width=25,bg="light blue1",command=self.cancel).place(x=709,y=77)
        Label(self.root,text="FRAME RATE:",bg="lavender").place(x=710,y=130)
        self.frLabel = Label(self.root,bg='black',width=14,fg="light green")
        self.frLabel.place(x=790,y=130)
        Label(self.root,text="N FRAMES:",bg="lavender").place(x=720,y=170)
        self.nframesLabel = Label(self.root,bg='black',width=14,fg="light green")
        self.nframesLabel.place(x=790,y=170)
        self.prog_bar = ttk.Progressbar(self.root)
        self.prog_bar.place(x=10,y=170,width=687)
        self.processLabel = Label(self.root,text="PROCESS",bg="lavender",width=97)
        self.processLabel.place(x=10,y=148)
        self.filter_method = ttk.Combobox(master=self.root,width=27)
        self.filter_method.place(x=710,y=210)
        self.filter_method["values"]=["Bilateral Filter","Blur","Median Blur","fastNlMeansDenoisingColored","Filter2D","pyrDown"]
        self.filter_method.set("Bilateral Filter")
 
        self.root.mainloop()
 
    def open_file(self):
        self.dir = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                        filetypes=(("mp4 files","*.mp4"),("avi files","*.avi"),("gif files","*.gif")))
        if self.dir:
            self.file = self.dir
 
            probe = ffmpeg.probe(self.file)
            self.video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
            self.nframes = (self.video_streams[0]['nb_frames'])
            self.height = (self.video_streams[0]['height'])
            self.fr = (self.video_streams[0]['avg_frame_rate'])
            self.vidName = (self.file).split("/")[-1]
            self.filename.set(self.vidName)
            self.frLabel.configure(text=self.fr)
            self.nframesLabel.configure(text=self.nframes)
 
    def aply_method(self,fr):
        if self.filter_method.get() == "Bilateral Filter":
            edit = cv.bilateralFilter(fr,9,75,75)
        elif self.filter_method.get() == "Blur":
            edit = cv.blur(fr,(5,5))
        elif self.filter_method.get() == "Median Blur":
            edit = cv.medianBlur(fr,5)
        elif self.filter_method.get() == "fastNlMeansDenoisingColored":
            edit = cv.fastNlMeansDenoisingColored(fr,None,20,10,7,21)
        elif self.filter_method.get() == "Filter2D":
            edit = cv.filter2D(fr,-1,np.ones((5,5),np.float32)/12)
        elif self.filter_method.get() == "pyrDown":
            edit = cv.pyrDown(fr)
        return edit
 
    def cancel(self):
        self.canceled = True
        self.processLabel.configure(text="CANCELLED")
        self.btnStart.configure(state='normal')
        self.btnSearch.configure(state='normal')
        self.prog_bar.step(0)
        self.counter = 0

        self.frames_list = []
 
    def create_new_video(self):
        frame_array = []
        self.counter = 0
        dif = 0
        self.question = "yes"
        if len(self.frames_list) > 0:
            for i in self.frames_list:
                if self.canceled == False:
                    self.counter+=1
                    #height, width  = i.shape #layers
                    height = i.shape[0]
                    width = i.shape[1]
                    size = (width,height)
 
                    for k in range(1):
                        frame_array.append(i)
 
                    percent = self.counter*100/int(self.nframes)
                    self.prog_bar.step(percent-dif)
                    self.processLabel.configure(text="CREATING VIDEO: {}%".format(int(percent)))
                    dif=percent
 
            name,ex = os.path.splitext(self.vidName)
            self.vid_name = (name+'('+self.filter_method.get().replace(" ","")+')'+'.mp4').replace(" ","_")
            if self.vid_name in os.listdir() and self.canceled == False:
                self.question = messagebox.askquestion("OVERWRITE?","{} already exists. Overwrite? [y/N].".format(self.vid_name))
 
            if self.question == "yes" and self.canceled == False:
                if self.vid_name in os.listdir():
                    os.remove(self.vid_name)
                frame_rate = eval(self.fr)
                out = cv.VideoWriter('filteredVideo.mp4',cv.VideoWriter_fourcc(*'XVID'), frame_rate, size)
                print("CREATING VIDEO...")
                print('FA:',len(frame_array))
                self.processLabel.configure(text="FINALIZING VIDEO...")
                for e in range(len(frame_array)):
                    out.write(frame_array[e])
 
                out.release()
 
                self.processLabel.configure(text="ADDING AUDIO...")
                vid = ffmpeg.input('filteredVideo.mp4')
                audi = ffmpeg.input('VidAudioInfo.mp3')
                if 'VidAudioInfo.mp3' in os.listdir():
                    ffmpeg.concat(vid,audi,v=1,a=1).output(self.vid_name).run()
                    print('BOTH')
                else:
                    ffmpeg.output(vid,self.vid_name).run()
                #final_video.save(self.vid_name)
 
            self.frames_list = []
 
    def filtering(self):
        if self.file:
            directory = filedialog.askdirectory()
            if directory:
                try:
                    os.chdir(directory)
                    self.btnStart.configure(state='disabled')
                    self.btnSearch.configure(state='disabled')
                    try:
                        self.processLabel.configure(text="GETTING AUDIO DATA...")
                        audio = AudioSegment.from_file(self.file)#
                        audio.export("VidAudioInfo.mp3",format="mp3")
                    except:
                        pass
                    self.currentDir.set(os.getcwd())
                    dif = 0
                    self.counter = 0
                    self.canceled = False
                    self.cam = cv.VideoCapture(self.file)
                    ret = True
 
                    while self.canceled == False and ret:
                        ret,frame = self.cam.read()
                        if ret:
                            self.counter+=1
                            edited_frame = self.aply_method(frame)
                            self.frames_list.append(edited_frame)
 
                            self.percent = self.counter*100/int(self.nframes)
                            self.prog_bar.step(self.percent-dif)
                            self.processLabel.configure(text="PROCESSING FRAMES: {} ({}%)".format((self.counter),int(self.percent)))
                            dif=self.percent
 
                    self.create_new_video()
                    self.processLabel.configure(text="PROCESS: ENDED")
                    if self.vid_name and self.canceled == False and self.question == "yes":
                        messagebox.showinfo("TASK COMPLETED","Created video \'{}\'.".format(self.vid_name))
                    if 'VidAudioInfo.mp3' in os.listdir():
                        os.remove('VidAudioInfo.mp3')
                    if 'filteredVideo.mp4' in os.listdir():
                        if not self.vid_name in os.listdir():
                            os.rename('filteredVideo.mp4',self.vid_name)
                        else:
                            os.remove('filteredVideo.mp4')
                except Exception as e:
                    messagebox.showwarning("UNEXPECTED ERROR",str(e))
                self.btnStart.configure(state='normal')
                self.btnSearch.configure(state='normal')
 
    def init_task(self):
        t = threading.Thread(target=self.filtering)
        t.start()
 
if __name__=="__main__":
    app()
