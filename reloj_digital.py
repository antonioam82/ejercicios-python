#import sys
from  tkinter import *
import time

def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time,bg="black",fg="green",font="Arial 50 bold")
	clock.after(200,times)


root=Tk()
root.geometry("492x250")
clock=Label(root,font=("times",50,"bold"))
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text="Reloj Digital",font="times 24 bold",fg="red")
digi.grid(row=0,column=2)

#nota=Label(root,text=" horas   minutos   segundos",font="Arial 15 bold")
#nota.grid(row=3,column=2)

root.mainloop()
