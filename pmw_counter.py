from tkinter import *
import Pmw

ventana = Tk()
Pmw.initialise(ventana)

counter1 = Pmw.Counter()
counter1.setentry(41)
counter1.increment()
counter1.pack(padx = 10, pady = 10)
#counter1.configure(increment=3)#ESPECIFICAR INCREMENTO

counter2 = Pmw.Counter(datatype = 'time',
                       increment = 60)
counter2.setentry('00:00:00')
counter2.configure(increment = 1 * 1/60 * 60) #cambiar incremento
counter2.pack(padx = 10, pady = 10)
counter2.configure(downarrow_background = 'green',
                  uparrow_background = 'red')
#print(counter2.get())
#print(counter2.cget('datatype'))

counter3 = Pmw.Counter(orient = 'vertical')
counter3.pack(padx = 10, pady = 10)
#print(counter3.cget('increment'))

counter4 = Pmw.Counter(
    hull_relief = 'sunken',
    hull_borderwidth = 5)
counter4.setentry(1982)
counter4.pack(padx = 10, pady = 10)
