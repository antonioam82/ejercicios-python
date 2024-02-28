import numpy as np
from scipy.io import wavfile
import argparse
import os

def generate_tone(args):
    name = args.destination
    duration = args.duration
    sample_rate = args.sample_rate
    frequency = args.frequency
    modulation_rate = args.modulation_rate
    modulation_type = args.modulation_type
    modulation_depth = args.modulation_depth
    scale = args.scale

    # Generar el tiempo
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generar la forma de onda base
    if args.signal == "sin":
        base_wave = np.sin(2 * np.pi * frequency * t)
    elif args.signal == "square":
        base_wave = np.sign(np.sin(2 * np.pi * frequency * t))
    elif args.signal == "triangle":
        base_wave = 2 * np.abs(t % (1 / frequency) - 0.5) - 1
    elif args.signal == "sawtooth":
        base_wave = 2 * (t % (1 / frequency)) * frequency - 1

    # Aplicar la modulación
    if modulation_type == "frequency":
        modulated_wave = np.sin(2 * np.pi * (frequency + modulation_depth * base_wave) * t)
    elif modulation_type == "amplitude":
        modulated_wave = (1 + modulation_depth * base_wave) * np.sin(2 * np.pi * frequency * t)

    # Normalizar y escalar la forma de onda
    modulated_wave /= np.max(np.abs(modulated_wave))
    modulated_wave *= scale

    # Escribir el archivo de audio
    wavfile.write(name, sample_rate, np.int16(modulated_wave))

    print("Modulated signal audio saved correctly.")

def main():
    parser = argparse.ArgumentParser(description="Generate modulated audio tones")
    parser.add_argument('-dest','--destination', type=str, default="modulated_audio_signal.wav", help="Destination file name")
    parser.add_argument('-dur','--duration', type=float, default=3, help="Audio duration, in seconds")
    parser.add_argument('-sr','--sample_rate', type=int, default=44100, help="Sample rate in Hz")
    parser.add_argument('-freq','--frequency', type=float, default=440, help="Base frequency in Hz")
    parser.add_argument('-mr','--modulation_rate', type=float, default=12, help="Modulation rate in Hz")
    parser.add_argument('-md','--modulation_depth', type=float, default=10, help="Modulation depth")
    parser.add_argument('-sig','--signal', default='sin', choices=['sin', 'square', 'triangle', 'sawtooth'], help="Base waveform")
    parser.add_argument('-mt','--modulation_type', default='frequency', choices=['frequency', 'amplitude'], help="Modulation type")
    parser.add_argument('-scl','--scale', default=32767, type=int, help="Sound scale")

    args = parser.parse_args()
    generate_tone(args)

if __name__ == '__main__':
    main()
