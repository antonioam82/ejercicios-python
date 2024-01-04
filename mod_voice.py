import pyaudio
import wave
import sounddevice as sd
import numpy as np
from pynput import keyboard
import os

os.chdir(r'C:\Users\Antonio\Documents\audios')

def apply_modulation(audio, modulation_frequency, fs):
    t = np.linspace(0, len(audio) / fs, len(audio), endpoint=False)
    modulation_signal = np.sin(2 * np.pi * modulation_frequency * t)
    return audio * (1 + 0.5 * modulation_signal)  # Ajusta la amplitud de modulación según sea necesario

def grabar_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "grabacion_modulada.wav"
    MODULATION_FREQUENCY = 5  # Frecuencia de modulación en Hz

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    print("Grabando... Presiona la barra espaciadora para detener la grabación.")

    # Función para detener la grabación cuando se presiona la barra espaciadora
    def on_press(key):
        if key == keyboard.Key.space:
            return False  # Detiene el listener

    # Listener para detectar la tecla presionada
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        if not listener.running:
            break

    print("Grabación detenida.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Convertir los frames grabados a un array NumPy
    audio_np = np.frombuffer(b''.join(frames), dtype=np.int16)

    # Aplicar modulación AM a la señal grabada
    modulated_audio = apply_modulation(audio_np, MODULATION_FREQUENCY, RATE)

    # Reproducir la señal modulada
    sd.play(modulated_audio, RATE)
    sd.wait()  # Esperar hasta que la reproducción termine completamente

    # Guardar la señal modulada como un archivo WAV
    '''with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(modulated_audio.tobytes())'''

grabar_audio()
