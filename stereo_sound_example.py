import numpy as np
from scipy.io import wavfile

# Parámetros del audio
frecuencia_muestreo = 44100  # Frecuencia de muestreo (44.1 kHz es estándar en audio)
duracion = 0.4  # Duración en segundos
frecuencia_tono = 440  # Frecuencia de la señal (por ejemplo, A4, 440 Hz)

# Tiempo
t = np.linspace(0, duracion, int(frecuencia_muestreo * duracion), endpoint=False)

# Crear las señales para los dos canales (estéreo)
canal_izquierdo = 0.5 * np.sin(2 * np.pi * frecuencia_tono * t)  # Señal sinusoidal en el canal izquierdo
#canal_derecho = 0.5 * np.sin(2 * np.pi * (frecuencia_tono + 100) * t)  # Canal derecho con una frecuencia diferente
canal_derecho = 0.5 * np.sin(2 * np.pi * frecuencia_tono * t)

# Combinar los canales en un solo arreglo estéreo
audio_estereo = np.column_stack((canal_izquierdo, canal_derecho))


# Convertir el audio a formato de enteros de 16 bits (WAV estándar)
audio_estereo_int16 = np.int16(audio_estereo * 32767)

# Guardar el archivo WAV en estéreo
wavfile.write('audio_estereo.wav', frecuencia_muestreo, audio_estereo_int16)
