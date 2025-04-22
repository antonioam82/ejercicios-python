import numpy as np
import sounddevice as sd
import time

# Parámetros
fs = 44100  # Frecuencia de muestreo
duracion_tono = 0.5  # duración del tono (segundos)
duracion_silencio = 0.1  # duración del silencio
frecuencia1 = 440  # Hz
frecuencia2 = 480  # Hz

# Tiempo para el tono
t = np.linspace(0, duracion_tono, int(fs * duracion_tono), endpoint=False)

# Crear el tono combinando las dos frecuencias
tono = 0.5 * (np.sin(2 * np.pi * frecuencia1 * t) + np.sin(2 * np.pi * frecuencia2 * t))

# Hacemos un bucle para sonar como un teléfono llamando
num_repeticiones = 7 # cuántos "ring" quieres hacer

for _ in range(num_repeticiones):
    # Reproducir el tono
    sd.play(tono, samplerate=fs)
    sd.wait()
    # Silencio
    time.sleep(duracion_silencio)
