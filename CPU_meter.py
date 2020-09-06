from tkinter import *
import psutil

def cpu_met():
    c = psutil.cpu_percent(interval = 1)
    cpu_label.config(text='{}%'.format(c))
    cpu_label.after(200,cpu_met)


ventana = Tk()
ventana.geometry("485x250")
ventana.title("CPU Usage")
cpu_label = Label(ventana,bg="black",fg="green",font="Arial 30 bold")
cpu_label.place(x=230,y=20)

digi=Label(ventana,text="CPU Usage:",font="arial 24 bold",fg="red")
digi.place(x=20,y=25)

cpu_met()

ventana.mainloop()
