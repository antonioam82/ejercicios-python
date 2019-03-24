#IMPORTAMOS LIBRERIAS NECESARIAS.
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

#------------------------------CREAR VENTANA---------------------------------
root = tkinter.Tk()
root.wm_title("Grafica insertada en Tkinter")


#------------------------------CREAR GRAFICA---------------------------------
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))#AÑADIR "subbplot"

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------------BOTÓN "cerrar"----------------------------------
def cerrar():
    root.quit()     
    root.destroy()

button = tkinter.Button(master=root, text="cerrar", command=cerrar)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
