import pyaudio
import numpy as np
import queue
import time
from pynput import keyboard as pk
import argparse
import functools
import sys
import time

CHANNELS = 1
RATE     = 44100
CHUNK    = 1024

grabando      = True
reproduciendo = False
terminado     = False
phase         = 0

def on_press(key):
    global grabando, reproduciendo
    if key == pk.Key.space and grabando:
        grabando      = False
        reproduciendo = True
        print("\nREPRODUCIENDO...")

def input_callback(audio_queue, frequency, in_data, frame_count, time_info, flag):
    global phase
    if grabando:
        audio = np.frombuffer(in_data, dtype=np.float32).copy()
        t     = (np.arange(frame_count) + phase) / RATE
        osc   = np.sin(2 * np.pi * frequency * t).astype(np.float32)
        audio *= osc
        try:
            audio_queue.put_nowait(audio.tobytes())
        except queue.Full:
            pass
    phase += frame_count
    return (None, pyaudio.paContinue)

def output_callback(audio_queue, in_data, frame_count, time_info, flag):
    global reproduciendo, terminado
    if reproduciendo:
        try:
            data = audio_queue.get_nowait()
        except queue.Empty:
            reproduciendo = False
            terminado     = True
            data = np.zeros(frame_count, dtype=np.float32).tobytes()
    else:
        data = np.zeros(frame_count, dtype=np.float32).tobytes()
    return (data, pyaudio.paContinue)

def start(audio_queue, frequency):
    p = pyaudio.PyAudio()

    in_dev  = p.get_default_input_device_info()
    out_dev = p.get_default_output_device_info()
    print(f"Entrada   : [{in_dev['index']}] {in_dev['name']}")
    print(f"Salida    : [{out_dev['index']}] {out_dev['name']}")
    print(f"Oscilador : {frequency} Hz")
    print(f"Buffer    : {audio_queue.maxsize} chunks "
          f"(~{audio_queue.maxsize * CHUNK / RATE:.1f}s)")
    print("\nGrabando desde el inicio. Pulsa ESPACIO para parar y reproducir.\n")

    cb_in  = functools.partial(input_callback,  audio_queue, frequency)
    cb_out = functools.partial(output_callback, audio_queue)

    stream_in = p.open(
        format=pyaudio.paFloat32, channels=CHANNELS,
        rate=RATE, input=True, frames_per_buffer=CHUNK,
        stream_callback=cb_in,
    )
    stream_out = p.open(
        format=pyaudio.paFloat32, channels=CHANNELS,
        rate=RATE, output=True, frames_per_buffer=CHUNK,
        stream_callback=cb_out,
    )

    stream_in.start_stream()
    stream_out.start_stream()

    listener = pk.Listener(on_press=on_press)
    listener.start()
    sec = 1
    try:
        while not terminado:
            if grabando:
                seg = audio_queue.qsize() * CHUNK / RATE
                sys.stdout.write(f"\rTIEMPO DE GRABACION: {sec} segundos")
                sys.stdout.flush()
                time.sleep(1)
                sec += 1
            elif reproduciendo:
                seg = audio_queue.qsize() * CHUNK / RATE
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n\nInterrumpido.")
    finally:
        print("\nCerrando...")
        listener.stop()
        stream_in.stop_stream();  stream_in.close()
        stream_out.stop_stream(); stream_out.close()
        p.terminate()
        print("Hasta luego.")

def main():
    parser = argparse.ArgumentParser(
        prog="audio_modulator.py",
        description="Voice modulator",
        conflict_handler="resolve",
    )
    parser.add_argument("-freq", "--frequency", type=float, default=440.0,help="Frecuencia del oscilador en Hz (default: 440)")
    #parser.add_argument("-max",  "--maxsize",   type=int, default=400,help="Tamaño máximo de la cola en chunks (default: 400)")
    parser.add_argument("-sec", "--seconds", type=int, default=5,help="Duracion de la grabacion, en segundos")
    
    args = parser.parse_args()
    maxsize = (args.seconds * RATE) / CHUNK
    audio_queue = queue.Queue(maxsize=maxsize)
    start(audio_queue, args.frequency)


if __name__ == "__main__":
    main()
