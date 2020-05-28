import numpy as np
import matplotlib.pyplot as plt

class ParOrdenado:
    def __init__(self,a,b):
        self.real = int(a)
        self.imaginario = int(b)

def graficarComp(e):
    x,y = e.real, e.imaginario

    izda = min(-1, x-1)
    dcha = max(1, x+1)
    abjo = min(-1, y-1)
    arba = max(1, y+1)

    plt.quiver([x],[y],angles='xy',scale_units='xy',scale=1)

    plt.axhline(0,color='black')
    plt.axvline(0,color='black')

    plt.xlim([izda,dcha])
    plt.ylim([abjo,arba])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('({},{})'.format(e.real,e.imaginario))
    plt.show()

ejemplo = ParOrdenado(1,2)
graficarComp(ejemplo)
