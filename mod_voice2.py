import pyaudio
import wave
import tempfile
import pydub
import pydub.playback
import sounddevice as sd
from colorama import Fore, Style, init
import numpy as np
from pynput import keyboard

init()

'''def apply_modulation(audio, modulation_frequency, fs):
    t = np.linspace(0, len(audio) / fs, len(audio), endpoint=False)
    modulation_signal = np.sin(2 * np.pi * modulation_frequency * t)
    return audio * (1 + 0.5 * modulation_signal)'''

def change_speed(input_audio, speed_factor):
    # Calcula la nueva tasa de fotogramas
    new_frame_rate = int(input_audio.frame_rate * speed_factor)
    # Sobrescribe el atributo frame_rate con la nueva tasa de fotogramas
    modified_audio = input_audio._spawn(input_audio.raw_data, overrides={"frame_rate": new_frame_rate})
    return modified_audio

def enter_speed_rate():
    while True:
        try:
            rate = float(input("Introduce factor velocidad: "))
            if rate > 0.0:
                return rate
            else:
                print(Fore.RED + Style.BRIGHT + "ERROR: El factor debe ser mayor a 0.0." + Fore.RESET + Style.RESET_ALL)
                
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Por favor, introduce un número válido." + Fore.RESET + Style.RESET_ALL)


def grabar_audio(r):
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

    print("Grabación detenida (reproduciendo resultado).")

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

            #modulated_audio = change_speed(input_audio, speed_factor)
            speed_factor = r#1.8 #2.0 #0.6
            modulated_audio = change_speed(input_audio, speed_factor)
            #modulated_audio = normalize_volume(input_audio)

            # Reproducir el audio modulado
            pydub.playback.play(modulated_audio)

            preg = input("¿Escriba 'S' para guardar?: ")
            if preg.upper() == "S":
                output_filename = "modulated_audio.wav"
                modulated_audio.export(output_filename, format="wav")
                print("Audio guardado correctamente")

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "ERROR: " , str(e) + Fore.RESET + Style.RESET_ALL)

rate = enter_speed_rate()
grabar_audio(rate)
    
