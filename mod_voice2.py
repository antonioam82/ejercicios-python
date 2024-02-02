import pyaudio
import wave
import tempfile
import pydub
import pydub.playback
import sounddevice as sd
import numpy as np
from pynput import keyboard

'''def apply_modulation(audio, modulation_frequency, fs):
    t = np.linspace(0, len(audio) / fs, len(audio), endpoint=False)
    modulation_signal = np.sin(2 * np.pi * modulation_frequency * t)
    return audio * (1 + 0.5 * modulation_signal)'''

def change_speed(input_audio, speed_factor):
    #modified_audio = input_audio.speedup(playback_speed=speed_factor) # cambia velocidad
    modified_audio = input_audio.reverse() # inversion audio
    return modified_audio

'''def normalize_volume(input_audio):
    audio = pydub.AudioSegment.from_file(input_audio)
    normalized_audio = pydub.effects.normalize(audio)
    return normalized_audio'''

def grabar_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
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

    try:
        # Escribir el audio grabado en un archivo temporal
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            tmp_filename = tmpfile.name
            wf = wave.open(tmp_filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            # Cargar el archivo temporal con pydub
            input_audio = pydub.AudioSegment.from_wav(tmp_filename)

            speed_factor = 1.0
            modulated_audio = change_speed(input_audio, speed_factor)
            #modulated_audio = normalize_volume(input_audio)

            # Reproducir el audio modulado
            pydub.playback.play(modulated_audio)

    except Exception as e:
        print("ERROR: " , str(e))

grabar_audio()
