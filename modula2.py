import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Configuración de la grabación
duration = 5  # Duración de la grabación en segundos
fs = 44100    # Frecuencia de muestreo (puedes ajustarla si es necesario)

# Función para grabar audio
def record_audio(duration, fs):
    print("Comenzando la grabación...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Grabación finalizada.")
    return recording

# Función para aplicar una modulación intensa al audio
def apply_modulation(audio, modulation_frequency, fs):
    t = np.linspace(0, len(audio) / fs, len(audio), endpoint=False)
    modulation_signal = np.sin(2 * np.pi * modulation_frequency * t)
    return audio * (1 + 1.5 * modulation_signal)  # Ajusta el factor de modulación según sea necesario

# Función para reproducir audio
def play_audio(audio, fs):
    print("Reproduciendo audio...")
    sd.play(audio, fs)
    sd.wait()

# Grabar audio durante la duración especificada
audio_recording = record_audio(duration, fs)

# Aplicar modulación intensa al audio grabado
modulated_audio = apply_modulation(audio_recording[:, 0], 10, fs)  # Frecuencia de modulación de 10 Hz



# Sobremodulación para aumentar la distorsión
modulated_audio = np.tanh(modulated_audio * 5)  # Ajusta el factor para controlar la distorsión

# Reproducir el audio modulado
play_audio(modulated_audio, fs)

# Guardar la grabación original y la modulada como archivos WAV
write("grabacion_original.wav", fs, audio_recording)
write("grabacion_distorsionada.wav", fs, modulated_audio)

print("Grabación original guardada como 'grabacion_original.wav'.")
print("Grabación distorsionada guardada como 'grabacion_distorsionada.wav'.")
