import pyaudio
import numpy as np
import queue
import time
from pynput import keyboard as pk
import argparse
import functools
import sys
from colorama import init, Fore, Style
from dataclasses import dataclass, field

#audio_modulator2.py -freq 650 -sec 8 -amp 9
#audio_modulator2.py -mod m1 -freq 1400 -sec 10 -amp 7
#audio_modulator2.py -mod m3 -freq 678 -sec 20 -amp 10

CHANNELS = 2
RATE     = 44100
CHUNK    = 1024

@dataclass
class AppState:
    grabando: bool = True
    reproduciendo: bool = False
    terminado: bool = False
    phase: int = 0

def on_press(state,key):
    if key == pk.Key.space and not state.reproduciendo:
        if state.grabando:
            state.grabando = False
        state.reproduciendo = True

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

'''def input_callback(audio_queue, frequency, amplitude, state, modulator, in_data, frame_count, time_info, flag):
    #global phase, grabando
    if state.grabando:
        audio = np.frombuffer(in_data, dtype=np.float32).copy()
        t = (np.arange(frame_count) + state.phase) / RATE

        if modulator == 'NORMAL':
            osc = np.sin(2 * np.pi * frequency * t).astype(np.float32)
        else:
            twopi   = 2 * np.pi
            if modulator == "m1":
                osc_tan = np.tan(np.sin(twopi * frequency * t))
                osc = amplitude * (np.clip(osc_tan, -1.5, 1.5) / 1.5).astype(np.float32)
            elif modulator == "m2":
                lfo_ancho = np.sin(twopi * 0.2 * t) * 0.4 + 0.5  # Modulación interna del ancho sin
                fase_cuadrada = np.mod(t * frequency, 1.0)
                osc = amplitude * ((fase_cuadrada < lfo_ancho).astype(np.float32) * 2.0 - 1.0)
            elif modulator == "m3":
                niveles = 6
                osc_seno = np.sin(twopi * frequency * t)
                osc = amplitude * (np.round(osc_seno * niveles) / niveles).astype(np.float32)
            elif modulator == "m4":
                fase = np.mod(t * frequency, 1.0)
                osc_tiburon = np.where(fase < 0.1, fase / 0.1, (1.0 - fase) / 0.9)
                osc = amplitude * (osc_tiburon * 2.0 - 1.0).astype(np.float32)
            elif modulator == "m5":
                modulador_fm = np.sin(twopi * (frequency * 1.5) * t) * 2.0
                osc = amplitude * (np.sin(twopi * frequency * t + np.exp(modulador_fm)).astype(np.float32))
            
        audio *= osc
        audio_queue.put(audio.tobytes())
    state.phase += frame_count
    return (None, pyaudio.paContinue)'''

def input_callback(audio_queue, frequency, amplitude, state, modulator, in_data, frame_count, time_info, flag):

    if flag:
        print(f"\nWarning input stream: {flag}")
        return (None, pyaudio.paContinue)
    
    if state.grabando:
        audio = np.frombuffer(in_data, dtype=np.float32).copy()
        # Mezclar canales estéreo a mono
        audio = audio.reshape(-1, 2).mean(axis=1)  # ← (frame_count, 2) → (frame_count,)

        t = (np.arange(frame_count) + state.phase) / RATE
        twopi = 2 * np.pi

        if modulator == 'NORMAL':
            osc = np.sin(twopi * frequency * t).astype(np.float32)
        elif modulator == "m1":
            osc_tan = np.tan(np.sin(twopi * frequency * t))
            osc = amplitude * (np.clip(osc_tan, -1.5, 1.5) / 1.5).astype(np.float32)
        elif modulator == "m2":
            lfo_ancho = np.sin(twopi * 0.2 * t) * 0.4 + 0.5
            fase_cuadrada = np.mod(t * frequency, 1.0)
            osc = amplitude * ((fase_cuadrada < lfo_ancho).astype(np.float32) * 2.0 - 1.0)
        elif modulator == "m3":
            niveles = 6
            osc_seno = np.sin(twopi * frequency * t)
            osc = amplitude * (np.round(osc_seno * niveles) / niveles).astype(np.float32)
        elif modulator == "m4":
            fase = np.mod(t * frequency, 1.0)
            osc_tiburon = np.where(fase < 0.1, fase / 0.1, (1.0 - fase) / 0.9)
            osc = amplitude * (osc_tiburon * 2.0 - 1.0).astype(np.float32)
        elif modulator == "m5":
            modulador_fm = np.sin(twopi * (frequency * 1.5) * t) * 2.0
            osc = amplitude * np.sin(twopi * frequency * t + np.exp(modulador_fm)).astype(np.float32)
        elif modulator == "m6":
            f2 = frequency * 1.007  # desafinación leve
            osc1 = np.sin(twopi * frequency * t)
            osc2 = np.sin(twopi * f2 * t)
            osc  = amplitude * (osc1 * osc2)
        elif modulator == "m7":
            osc = np.sin(twopi * frequency * t)
            drive = amplitude * 8.0
            osc = amplitude * np.tanh(drive * osc) / np.tanh(drive)
        elif modulator == "m8":
            lfo_rate = 5.0  # Hz del tremolo
            lfo = 0.5 + 0.5 * np.sin(twopi * lfo_rate * t)
            osc = amplitude * np.sin(twopi * frequency * t) * lfo

        audio *= osc

        estereo = np.stack([audio, audio], axis=1).flatten()
        audio_queue.put(estereo.tobytes())

    state.phase += frame_count
    return (None, pyaudio.paContinue)

'''def output_callback(audio_queue, state, in_data, frame_count, time_info, flag):
    #global reproduciendo, terminado
    if state.reproduciendo:
        try:
            data = audio_queue.get_nowait()
        except queue.Empty:
            state.reproduciendo = False
            state.terminado     = True
            data = np.zeros(frame_count, dtype=np.float32).tobytes()
    else:
        data = np.zeros(frame_count, dtype=np.float32).tobytes()
    return (data, pyaudio.paContinue)'''

def output_callback(audio_queue, state, show_stream, in_data, frame_count, time_info, flag):

    if flag:
        print(f"\nWarning output stream: {flag}")
        return (np.zeros(frame_count * 2, dtype=np.float32).tobytes(), pyaudio.paContinue)
    
    if state.reproduciendo:
        try:
            data = audio_queue.get_nowait()
            if show_stream:
                print(" ".join(f"{b:08b}" for b in data[:16]) + " ...")########################################
            #print(" ".join(f"{b:08b}" for b in data))
            ####################################################################################################
            '''# Tomamos una muestra representativa (el primer canal del primer frame)
            valores = np.frombuffer(data, dtype=np.float32)
            muestra = valores[0]
            
            # Mapeamos el valor (-1.0 a 1.0) a una barra de texto de un ancho máximo de 40 caracteres
            ancho_maximo = 40
            centro = ancho_maximo // 2
            posicion = int(centro + (muestra * centro))
            posicion = max(0, min(ancho_maximo - 1, posicion)) # Asegurar límites
            
            # Construimos la línea visual
            linea = [" "] * ancho_maximo
            linea[centro] = "|" # Eje central (silencio)
            linea[posicion] = "O" # Posición actual de la onda
            
            # Imprimimos la línea en la terminal
            print("".join(linea))
            # --- FIN DEL GRÁFICO ---
            '''######################################################################################################
            
        except queue.Empty:
            state.reproduciendo = False
            state.terminado     = True
            data = np.zeros(frame_count * 2, dtype=np.float32).tobytes()  # ← *2
    else:
         #print(data)
        data = np.zeros(frame_count * 2, dtype=np.float32).tobytes()  # ← *2
        #print(data)
    return (data, pyaudio.paContinue)

def check_name(m):
    modulators = ['NORMAL','m1','m2','m3','m4','m5','m6','m7','m8']
    if m not in modulators:
        raise argparse.ArgumentTypeError(
            Fore.RED + Style.BRIGHT +
            f"'{m}' is not a valid modulator name." +
            Fore.RESET + Style.RESET_ALL
        )
    return m

def start(audio_queue, frequency, amplitude, seconds, state, modulator, show_stream):
    #global grabando, reproduciendo, terminado

    p = pyaudio.PyAudio()

    in_dev  = p.get_default_input_device_info()
    out_dev = p.get_default_output_device_info()
    print(f"Entrada   : [{in_dev['index']}] {in_dev['name']}")
    print(f"Salida    : [{out_dev['index']}] {out_dev['name']}")
    print(f"Oscilador : {frequency} Hz")
    print(f"Duracion  : {seconds:.1f}s")
    print("\nGrabando desde el inicio. Pulsa ESPACIO para parar y reproducir.\n")

    cb_in  = functools.partial(input_callback,  audio_queue, frequency, amplitude, state, modulator)
    cb_out = functools.partial(output_callback, audio_queue, state, show_stream)

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

    listener = pk.Listener(on_press=functools.partial(on_press, state))
    listener.start()

    start_time = time.time()
    try:
        while not state.terminado:
            if state.grabando:
                elapsed = time.time() - start_time
                sys.stdout.write(f"\rTIEMPO DE GRABACION: {elapsed:.1f} s / {seconds:.1f} s")
                sys.stdout.flush()
                if elapsed >= seconds:
                    state.grabando = False
                    print("\nTiempo agotado. Pulsa ESPACIO para reproducir...")
                    while not state.reproduciendo:
                        time.sleep(0.05)
                    #print("REPRODUCIENDO...")
            elif state.reproduciendo:
                if not show_stream:
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

def main():
    parser = argparse.ArgumentParser(
        prog="audio_modulator.py",
        description="Voice modulator",
        conflict_handler="resolve",
    )
    parser.add_argument("-freq","--frequency",type=check_positive, default=440.0,help="Frecuencia del oscilador en Hz (default: 440)")
    parser.add_argument("-sec","--seconds",type=check_positive, default=5.0,help="Duracion de la grabacion, en segundos")
    parser.add_argument("-mod","--modulator",type=check_name,default="NORMAL",help="Modulator")
    parser.add_argument("-amp","--amplitude",type=check_positive, default=1.0,help="Amplitud")
    parser.add_argument("-sd","--stream_data",action="store_true",help="Show stream audio data")

    args = parser.parse_args()
    state = AppState()
    audio_queue = queue.Queue()
    start(audio_queue, args.frequency, args.amplitude, args.seconds, state, args.modulator, args.stream_data)

if __name__ == "__main__":
    main()

