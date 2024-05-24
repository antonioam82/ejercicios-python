import numpy as np
import matplotlib.pyplot as plt

A_m = 5 #amplitud de la moduladora
f_m = 4000 #frecuaencia de la moduladora
A_p = 5 #amplitud de la portadora
f_p = 40000#40000 #frecuencia de la portadora
ka = 3 #indice de modulacion
t = np.linspace(0, 1, 1000)

moduladora = A_m*np.cos(2*np.pi*f_m*t)
portadora = A_p*np.cos(2*np.pi*f_p*t)
modulacion_AM = A_p*(1+ka*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_p*t)

# señal moduladora
plt.subplot(3,1,1)
plt.title("Señal de Mensaje o Moduladora")
plt.plot(moduladora,'g')
plt.ylabel('Amplitud')

# señal portadora
plt.subplot(3,1,2)
plt.title("Señal Portadora")
plt.plot(portadora,'r')
plt.ylabel('Amplitud')

# señal AM
plt.subplot(3,1,3)
plt.title("Modulacion AM")
plt.plot(modulacion_AM, color='purple')
plt.ylabel('Amplitud')
plt.xlabel('Señal AM')

plt.show()
