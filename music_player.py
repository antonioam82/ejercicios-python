#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog, messagebox
import random
import wave
import pyaudio
import threading
import json
import time
import os
 
if not "data.json" in os.listdir():
    d = {}
    with open("data.json", "w") as f:
        json.dump(d, f)
        print("created data.json")
 
class Player:
    def __init__(self):
        self.root = Tk()
        self.root.title("Music Player")
        self.root.configure(bg="gray78")
        self.root.geometry("923x306")
        self.CHUNK = 1024
 
        with open("data.json") as f:
            self.audio_list = json.load(f)
 
        self.filename = StringVar()
        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.file_path = None
        self.playing = False
        self.my_list = []
        self.any_selected = False
        self.playall_mode = False
        self.random_mode = False
        self.counting = 0
 
        entryDir = Entry(self.root,textvariable=self.currentDir,width=153)
        entryDir.place(x=0,y=0)
        self.timer = Label(self.root,text="0:00:00",bg="black",fg="green",font=("arial","34"),width=13,height=2)
        self.timer.place(x=9,y=28)
        self.entryFile = Entry(self.root,textvariable=self.filename,width=37,font=("arial",20))
        self.entryFile.place(x=355,y=28)
        Button(self.root,text="SEARCH",width=78,bg="blue",fg="white",command=self.open_file).place(x=356,y=75)
        Button(self.root,text="PLAY",width=15,bg="goldenrod1",command=self.init_task).place(x=356,y=108)
        Button(self.root,text="STOP",width=15,bg="goldenrod1",command=self.stop_music).place(x=474,y=108)
        Button(self.root,text="ADD TO PLAYLIST",width=44,bg="goldenrod1",command=self.add).place(x=594,y=108)#self.add
        self.items = Label(self.root,text=('{} ITEMS'.format(len(self.audio_list))),font=("arial",10),width=39,height=2,bg="black",fg="red")
        self.items.place(x=594,y=147)
        Button(self.root,text="REMOVE PLAYLIST",width=44,command=self.remove_playlist).place(x=594,y=220)#215
        Button(self.root,text="REMOVE FROM PLAYLIST",width=44,command=self.remove_from_list).place(x=594,y=190)#249
        self.btnPlayall = Button(self.root,text="PLAY ALL",width=21,height=2,command=self.init_task2)
        self.btnPlayall.place(x=594,y=254)
        self.btnRandom = Button(self.root,text="RANDOM MODE: OFF",width=21,height=2,command=self.act_random)
        self.btnRandom.place(x=755,y=254)
        self.canvas = Canvas(self.root)
        self.canvas.place(x=9,y=147)
        self.scrollbar = Scrollbar(self.canvas,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.fav_list = Listbox(self.canvas,width=93,height=9,bg="gray96")
        self.fav_list.pack()
        self.fav_list.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.fav_list.yview)
 
        self.show_list()
 
        self.root.mainloop()
 
    #INICIA PROCESO EN PARALELO.
    def init_task(self):
        if self.playall_mode == False and self.playing == False:
            self.any_selected = self.is_any_selected()
            if self.any_selected:
                print("OK")
 
                self.file_path = self.my_list[self.fav_list.curselection() [ 0 ] ]
                self.key = self.get_key(self.file_path)
                self.filename.set(self.key)
            if self.file_path: #and self.playing == False:
                if os.path.exists(self.file_path):
                    self.clear_counter()
                    t = threading.Thread(target=self.music)
                    t.start()
                else:
                    messagebox.showwarning("FILE NOT FOUND",'''Path not found, file may have
been deleted or moved.''')
 
    def remove_playlist(self):
        if self.fav_list.size() > 0:
            message = messagebox.askquestion("REMOVE PLAYLIST",'Do you want to remove all the playlist?')
            if message == "yes":
                self.playing = False
                self.playall_mode = False###################
                self.btnPlayall.configure(text="PLAY ALL")
                self.my_list = []
                self.fav_list.delete(0,END)
                self.audio_list = {}
                d = {}
                with open("data.json", "w") as f:
                    json.dump(d, f)
                self.items.configure(text='0 ITEMS')
 
    #AÑADE ELEMENTO AL LISTBOX.
    def add(self):
        if self.entryFile.get() != "" and self.playall_mode == False:
            self.fav_list.delete(0,END)
            self.audio_list[self.filename.get()]=self.file_path
            with open("data.json", "w") as f:
                json.dump(self.audio_list, f)
            self.show_list()
            self.items.configure(text='{} ITEMS'.format(len(self.audio_list)))
 
    def remove_from_list(self):
        if self.fav_list.size() > 0:
            self.any_selected = self.is_any_selected()
            if self.any_selected:
                self.playing = False
                self.playall_mode = False###################
                message = messagebox.askquestion("REMOVE ITEM",'Delete selected item from playlist?')
                if message == "yes":
                    #self.size_ -= 1
                    self.file_path = self.my_list[self.fav_list.curselection()[ 0 ] ]
                    self.key = self.get_key(self.file_path)
                    del self.audio_list[self.key]
                    with open("data.json", "w") as f:
                        json.dump(self.audio_list, f)
                    self.fav_list.delete(0,END)
                    self.show_list()
                    self.items.configure(text='{} ITEMS'.format(len(self.audio_list)))
            else:
                messagebox.showwarning("NO ITEM SELECTED","Select the item you want to delete.")
 
    def show_list(self):
        if len(self.audio_list) > 0:
            self.my_list = []
            c=1
            for i in (self.audio_list):
                self.fav_list.insert(END,(str(c)+"- "+i))
                self.my_list.append(self.audio_list[i])
                c+=1
 
    def is_any_selected(self):
        sel = False
        self.num_selected = 0
        for i in range(0,self.fav_list.size()):
            if self.fav_list.selection_includes(i):
                self.num_selected += 1
                sel = True
                break
        print("NUmber: ",self.num_selected)
        return sel
 
    def open_file(self):
        self.stop_music()
        self.any_selected = self.is_any_selected()
        if self.any_selected:
            self.fav_list.selection_clear(self.fav_list.curselection() [ 0 ] )
        fpath = filedialog.askopenfilename(initialdir = "/",title = "Select File",
                        filetypes = (("wav files","*.wav"),("all files","*.*")))
        if fpath:
            if fpath.endswith(".wav"):
                self.file_path = fpath
                self.filename.set(self.file_path.split("/")[-1])
            else:
                messagebox.showwarning("ERROR","Bad file format.")
 
    #FINALIZA AUDIO
    def stop_music(self):
        if self.playing == True:
            self.playing = False
            print("STOPPED")
        if self.playall_mode == True:
            self.playall_mode = False
            self.btnPlayall.configure(text="PLAY ALL")
 
    def clear_counter(self):
        self.sec_counter = 0
        self.min_counter = 0
        self.hour_counter = 0
 
    def counter_format(self,c):
        if c<10:
            c="0"+str(c)
        return c
 
    def timer_count(self):
        if self.playing == True:
            self.timer['text'] = str(self.hour_counter)+":"+str(self.counter_format(self.min_counter)
                                                    )+":"+str(self.counter_format(self.sec_counter))
            self.sec_counter+=1
            if self.sec_counter==60:
                self.sec_counter=0
                self.min_counter+=1
            if self.min_counter==60:
                self.min_counter=0
                self.hour_counter+=1
            self.process=self.timer.after(1000,self.timer_count)
        else:
            self.timer.after_cancel(self.process)
 
    def init_task2(self):
        if self.playall_mode == False and self.playing == False:####################################################
            self.is_any_selected()
            if self.num_selected > 0:
                self.fav_list.selection_clear(self.fav_list.curselection() [ 0 ] )####################################################################
                #print(self.fav_list.curselection())
            if self.fav_list.size() > 0:
                self.btnPlayall.configure(text="PLAYING ALL...")
                self.playall_mode = True
                t2 = threading.Thread(target=self.count)
                t2.start()
            else:
                messagebox.showwarning("EMPTY PLAYLIST","No item on playlist.")
        else:
            messagebox.showwarning("CAN'T ACTVATE","You must stop current audio to use this function.")
 
    def define_index(self):
        if self.random_mode == True:
            self.counting = random.randint(0,len(self.audio_list))
        self.counting += 1
        if self.counting >= len(self.audio_list):
            self.counting = 0
 
    def act_random(self):
        if self.random_mode == True:
            self.random_mode = False
            self.btnRandom.configure(text="RANDOM MODE: OFF")
        else:
            self.random_mode = True
            self.btnRandom.configure(text="RANDOM MODE: ON")
 
    def count(self):
        #self.size_ = len(self.audio_list)
        if self.random_mode == True:
            self.counting = random.randint(0,(len(self.audio_list))-1)
        else:
            self.counting = 0
        while self.playall_mode == True:
            print(self.counting)
            print("SIZE: ",len(self.audio_list))
            if self.playall_mode == True:
                self.clear_counter()
                self.fav_list.selection_set(self.counting)
                self.fav_list.see(self.counting)
                time.sleep(1)
                print("COUNTING: ",self.counting)
                self.filename.set(self.my_list[self.counting].split("/")[-1])
                self.file_path = self.my_list[self.fav_list.curselection() [ 0 ] ]
                if os.path.exists(self.file_path):
                    self.music()
                else:
                    messagebox.showwarning("FILE NOT FOUND",'''Path not found, file may have
been deleted or moved.''')
                    self.fav_list.selection_clear(self.fav_list.curselection() [ 0 ] )
                self.define_index()
        self.btnPlayall.configure(text="PLAY ALL")
 
    #REPRODUCE AUDIO.
    def music(self):
        try:
            self.playing = True
            self.p = pyaudio.PyAudio()
            wf = wave.open(self.file_path, 'rb')
            self.stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
            data = wf.readframes(self.CHUNK)
            self.timer_count()
            while data and self.playing == True:
                self.stream.write(data)
                data = wf.readframes(self.CHUNK)
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            if self.playall_mode == True:
                self.fav_list.selection_clear(self.fav_list.curselection() [ 0 ] )
            print("ENDED")
 
        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))
        self.playing = False
 
    def get_key(self,val):
        for key, value in self.audio_list.items():
            if val == value:
                return key
 
if __name__=="__main__":
    Player()
