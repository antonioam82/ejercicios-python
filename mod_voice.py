import pyaudio
import wave
import sounddevice as sd
import numpy as np
from pynput import keyboard

def apply_modulation(audio, modulation_frequency, fs):
    t = np.linspace(0, len(audio) / fs, len(audio), endpoint=False)
    modulation_signal = np.sin(2 * np.pi * modulation_frequency * t)
    return audio * (1 + 0.5 * modulation_signal)

def grabar_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "grabacion_modulada.wav"
    MODULATION_FREQUENCY = 5

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    print("Grabando... Presiona la barra espaciadora para detener la grabación.")

    def on_press(key):
        if key == keyboard.Key.space:
            return False  # Detiene el listener

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

    audio_np = np.frombuffer(b''.join(frames), dtype=np.int16)

    modulated_audio = apply_modulation(audio_np, MODULATION_FREQUENCY, RATE)

    sd.play(modulated_audio, RATE)
    sd.wait()  # Esperar hasta que la reproducción termine completamente

    '''with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(modulated_audio.tobytes())'''

grabar_audio()
