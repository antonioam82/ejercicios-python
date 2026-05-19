import pyaudio
import numpy as np
import queue
import time
from pynput import keyboard as pk
import argparse
import functools
import sys
from colorama import init, Fore, Style

CHANNELS = 1
RATE     = 44100
CHUNK    = 1024

grabando = True
reproduciendo = False
terminado = False
phase = 0

def on_press(key):
    global grabando, reproduciendo
    if key == pk.Key.space and not reproduciendo:
        if grabando:
            grabando = False
        reproduciendo = True
        #print("\nREPRODUCIENDO...")

def check_positive(v):
    value = float(v)
    if value <= 0:
        init()
        raise argparse.ArgumentTypeError(
            Fore.RED + Style.BRIGHT +
            f"Frequency and seconds must be greater than 0 ('{v}' is not valid)." +
            Fore.RESET + Style.RESET_ALL
        )
    return value

def input_callback(audio_queue, frequency, amplitude, in_data, frame_count, time_info, flag):
    global phase, grabando
    if grabando:
        audio = np.frombuffer(in_data, dtype=np.float32).copy()
        t     = (np.arange(frame_count) + phase) / RATE

        twopi   = 2 * np.pi
        osc_tan = np.tan(np.sin(twopi * frequency * t))
        osc     = amplitude * (np.clip(osc_tan, -1.5, 1.5) / 1.5).astype(np.float32)

        audio *= osc
        audio_queue.put(audio.tobytes())
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

def start(audio_queue, frequency, amplitude, seconds):
    global grabando, reproduciendo, terminado

    p = pyaudio.PyAudio()

    in_dev  = p.get_default_input_device_info()
    out_dev = p.get_default_output_device_info()
    print(f"Entrada   : [{in_dev['index']}] {in_dev['name']}")
    print(f"Salida    : [{out_dev['index']}] {out_dev['name']}")
    print(f"Oscilador : {frequency} Hz")
    print(f"Duracion  : {seconds:.1f}s")
    print("\nGrabando desde el inicio. Pulsa ESPACIO para parar y reproducir.\n")

    cb_in  = functools.partial(input_callback,  audio_queue, frequency, amplitude)
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

    start_time = time.time()
    try:
        while not terminado:
            if grabando:
                elapsed = time.time() - start_time
                sys.stdout.write(f"\rTIEMPO DE GRABACION: {elapsed:.1f} s / {seconds:.1f} s")
                sys.stdout.flush()
                if elapsed >= seconds:
                    grabando = False
                    print("\nTiempo agotado. Pulsa ESPACIO para reproducir...")
                    while not reproduciendo:
                        time.sleep(0.05)
                    #print("REPRODUCIENDO...")
            elif reproduciendo:
                seg = audio_queue.qsize() * CHUNK / RATE
                sys.stdout.write(f"\rREPRODUCIENDO... {seg:.1f}s RESTANTES    ")
                sys.stdout.flush()
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
    parser.add_argument("-freq", "--frequency", type=check_positive, default=440.0,help="Frecuencia del oscilador en Hz (default: 440)")
    parser.add_argument("-sec",  "--seconds",   type=check_positive, default=5.0,help="Duracion de la grabacion, en segundos")
    parser.add_argument("-amp",  "--amplitude", type=check_positive, default=1.0,help="Amplitud")

    args = parser.parse_args()
    audio_queue = queue.Queue()
    start(audio_queue, args.frequency, args.amplitude, args.seconds)


if __name__ == "__main__":
    main()
