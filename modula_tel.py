#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.io import wavfile
from scipy.signal import sawtooth
import argparse
from playsound3 import playsound
import sounddevice as sd
from pynput import keyboard
import os

def write_data(name, signal, duration, sample_rate, frequency, modulation_rate, scale, lfo):
    base_name, ex = os.path.splitext(name)
    
    with open(name.replace('.wav', '_data.txt'), 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Signal: {signal}\n")
        file.write(f"Duration: {duration} seconds\n")
        file.write(f"Sample Rate: {sample_rate} Hz\n")
        file.write(f"Frequency: {frequency} Hz\n")
        file.write(f"Modulation Rate: {modulation_rate} Hz\n")
        file.write(f"Scale: {scale}\n")
        file.write(f"LFO: {lfo}")
    print(f"\033[33mSaved signal info in '{base_name}_data.txt'.\033[0m")

def check_extension(file):
    name, ex = os.path.splitext(file)
    if ex == ".wav":
        return file
    else:
        raise argparse.ArgumentTypeError(f"\033[31mresult file must have '.wav' extension.\033[0m")

def play(file_name):
    sample_rate, audio_data = wavfile.read(file_name)
    sd.play(audio_data, sample_rate)

    def on_press(key):
        if key == keyboard.Key.space:
            sd.stop()
            print("\033[33mSound stopped by user.\033[0m")
            return False

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    sd.wait()
    listener.stop()
    
def generate_tone(args):
    name = args.destination
    duration = args.duration
    sample_rate = args.sample_rate
    frequency = args.frequency
    modulation_rate = args.modulation_rate
    signal = args.signal
    scale = args.scale
    lfo = args.lfo_rate
    write = args.write_data

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
 
    if signal == "sqrt":
        modulation_wave = np.sign(np.sin(2 * np.pi * lfo * t)) #10
    elif signal == "sin":
        modulation_wave = np.sin(2 * np.pi * lfo * t)
    elif signal == "trg":
        modulation_wave  = np.abs(sawtooth(2 * np.pi * lfo * t, width=0.5)) - 0.5  # 8 Hz
    elif signal == "swt":
        modulation_wave = sawtooth(2 * np.pi * lfo * t) #6

    
    modulated_wave = np.sin(2 * np.pi * (frequency + modulation_rate * modulation_wave) * t)
    modulated_wave /= np.max(np.abs(modulated_wave), axis=0)
    wavfile.write(name, sample_rate, np.int16(modulated_wave * scale))
    if write:
        write_data(name, signal, duration, sample_rate, frequency, modulation_rate, scale, lfo)
    

def main():
    parser = argparse.ArgumentParser(prog="MODULA_TEL 0.1", description="Generate modulated audio tones and phone ring tones")
    parser.add_argument('-dest', '--destination', type=check_extension, default="modulated_audio_signal.wav", help="Destination file name")
    parser.add_argument('-dur', '--duration', type=int, default=2, help="Audio duration, in seconds (ignored in ring mode)")
    parser.add_argument('-sr', '--sample_rate', type=int, default=44100, help="Sample rate in Hz")
    parser.add_argument('-lfo', '--lfo_rate', type=int, default=10, help="Low Frequency Oscillator value")
    parser.add_argument('-freq', '--frequency', type=int, default=440, help="Base frequency in Hz")
    parser.add_argument('-mr', '--modulation_rate', type=int, default=12, help="Modulation rate in Hz (ignored in ring mode)")
    parser.add_argument('-play', '--play_audio', action='store_true', help="Play modulated signal")
    parser.add_argument('-wr', '--write_data', action='store_true', help="Create text file with audio data")
    parser.add_argument('-sig', '--signal', default='sqrt', choices=['sin', 'sqrt', 'trg', 'swt'], help="Modulation wave (ignored in ring mode)")
    parser.add_argument('-scl', '--scale', default=32767, type=int, help="Sound scale")

    args = parser.parse_args()
    generate_tone(args)
    if args.play_audio:
        play(args.destination)


if __name__ == '__main__':
    main()
