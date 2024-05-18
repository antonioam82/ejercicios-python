import numpy as np
import matplotlib.pyplot as plt

# Configuración de parámetros
fs = 400  # Frecuencia de muestreo
Ec = 5  # Voltaje pico de la portadora
fc = 20  # Frecuencia de la portadora
fm = 1  # Frecuencia de la moduladora
m = 0.8  # Índice de modulación

Nc = 2  # Número de ciclos que se mostrará en la gráfica
t = np.arange(0, Nc/fm, 1/fs)  # Vector de tiempo

# Generación de señales
Vc = Ec * np.sin(2 * np.pi * fc * t)  # Señal portadora
Vmod = m * Ec * np.sin(2 * np.pi * fm * t)  # Señal moduladora
Vam = (1 + m * np.sin(2 * np.pi * fm * t)) * Ec * np.sin(2 * np.pi * fc * t)  # Señal AM

# Creación de la figura y los ejes
fig, ax = plt.subplots(figsize=(15, 7))
ax.set_title('Modulación AM')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Amplitud')
ax.grid(True)

# Graficar las señales
ax.plot(t, Vc + 15, label='Portadora', color='b')  # Desplazar la portadora para visualizar mejor
ax.plot(t, Vmod + 5, label='Moduladora', color='r')  # Desplazar la moduladora para visualizar mejor
ax.plot(t, Vam, label='Señal AM', color='k')

# Configuración de leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
