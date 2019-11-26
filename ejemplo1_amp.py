#IMPORTAMOS LIBRERIAS.
import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp

#INTRODUCIMOS DATOS.
x = np.linspace(0, 1, 50)
t = np.linspace(0, 1, 20)

X, T = np.meshgrid(x, t)
Y = np.sin(2*np.pi*(X+T))

#CREAMOS OBJETO "timeline".
timeline = amp.Timeline(t, units='s', fps=20)

#GENERAMOS ANIMACIÓN.
block = amp.blocks.Line(X, Y, marker=".", linestyle="-", color="r")
anim = amp.Animation([block],timeline)

#DEFINICIÓN DE ETIQUETAS PARA TITULO Y EJES.
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("y")

#GUARDAMOS ANIMACIÓN.
anim.save_gif('graph_anim.gif')

#INTRODUCIMOS LÍNEA DE TIEMPO
#Y BOTÓN PAUSE/PLAY
anim.controls()

#REPRESENTAMOS GRÁFICA.
plt.show()
