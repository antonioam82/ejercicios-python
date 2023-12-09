import numpy as np
from scipy.io import wavfile

# Parámetros de la señal de audio
duration = 3  # Duración en segundos
sample_rate = 44100  # Frecuencia de muestreo en Hz
frequency = 440  # Frecuencia base en Hz
modulation_rate = 5  # Frecuencia de modulación en Hz

# Crear la señal base (portadora)
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
carrier_wave = np.sin(2 * np.pi * frequency * t)

# Señal de modulación
modulation_wave = np.sin(2 * np.pi * modulation_rate * t)

# Modulación de la señal base
modulated_wave = np.sin(2 * np.pi * (frequency + modulation_rate * modulation_wave) * t)

# Normalizar para asegurarse de que esté en el rango de -1 a 1
modulated_wave /= np.max(np.abs(modulated_wave), axis=0)

# Guardar la señal modulada en un archivo de audio
wavfile.write('modulated_audio.wav', sample_rate, np.int16(modulated_wave * 32767))

print("Señal de audio modulada guardada correctamente.")
