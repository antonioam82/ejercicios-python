import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
from math import pi
import pylab as pl
from math import log10

plt.close('all')

Vm= float(input("Amplitud de la Moduladora: "))
Fm= float(input("Frecuancia de la Moduladora: "))
Vc= float(input("Amplitud de la Portadora: "))
Fc= float(input("Frecuencia de la Portadora: "))
kf= float(input("Factor de sensibilidad de frecuencia: "))
n= float(input("Numero de periodos: "))
print("")

z = 50
Af = kf*Vm
B = Af/Fm

Fs = 50000 # Frecuencia de muestreo
x = 0
n0 = [] 
bessel = []
f = np.arange(0,10,1)

# ECUACIONES PARA HALLAR BESSEL
for i in range(0,len(f)):
    x = round(sp.jv(i,B),2)
    bessel.append(x)

print(bessel)
