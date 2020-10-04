from tkinter import *
import pyaudio
import threading

class App:
    def __init__(self):

        self.CHUNK = 1024#1024
        WIDTH = 2
        CHANNELS = 2
        RATE = 44100
        #RECORD_SECONDS = 10
        self.playing = False

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=self.CHUNK)

        

        self.ventana = Tk()
        self.ventana.geometry("480x140")

        self.btnPlay = Button(self.ventana,text="START DEMO",width=10,command=self.playing_state)
        self.btnPlay.place(x=100,y=50)

        self.ventana.mainloop()

    def playing_v(self):
        print("* playing")
        while self.playing == True:
            data = self.stream.read(self.CHUNK)
            self.stream.write(data,self.CHUNK)

    def playing_state(self):
        if self.playing == False:
            self.playing = True
            t = threading.Thread(target=self.playing_v)
            t.start()
        else:
            self.playing = False
            print("* stopped")

    def terminate_p(self):
        print("TERMINATING")
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.t.join()


    def __del__(self):
        self.terminate_p()

if __name__=="__main__":
    App()
