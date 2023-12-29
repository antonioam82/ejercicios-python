import numpy as np
import matplotlib.pyplot as plt
from playsound import playsound
import sounddevice as sd

A_m = 470 # amplitud señal moduladora
f_m = 120 # frecuencia de la moduladora
A_p = 100 # amplitud de la portadora
f_p = 420 # frecuencia de la portadora
ka = 500 # indice de modulacion
duration = 3


t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
#t = np.linspace(0, duration, 3000)

moduladora = A_m*np.cos(2*np.pi*f_m*t)
portadora = A_p*np.cos(2*np.pi*f_p*t)
modulacion_AM = A_p*(1+ka*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_p*t)

plt.subplot(3,1,1)
plt.title('Señal de Mensaje o Moduladora')
plt.plot(moduladora,'g')
plt.ylabel('Amplitud')

plt.subplot(3,1,2)
plt.title('Señal Portadora')
plt.plot(portadora,'r')
plt.ylabel('Amplitud')

plt.subplot(3,1,3)
plt.title('Modulacion AM')
plt.plot(modulacion_AM, color='purple')
plt.ylabel('Amplitud')
plt.xlabel('Señal AM')

plt.show()

# Reproducir la señal modulada
print("Reproduciendo Señal Moduladora")
sd.play(moduladora, samplerate=44100)
sd.wait()
print("Reproduciendo Señal Portadora")
sd.play(portadora, samplerate=44100)
sd.wait()
print("Reproduciendo Señal Modulada")
sd.play(modulacion_AM, samplerate=44100)  # Puedes ajustar el samplerate según sea necesario
sd.wait()
