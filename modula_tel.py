#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.io import wavfile
from scipy.signal import sawtooth
import argparse
from playsound3 import playsound
from colorama import init, Fore, Style
import sounddevice as sd
import os

def check_extension(file):
    name, ex = os.path.splitext(file)
    if ex == ".wav":
        return file
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + f"result file must have '.wav' extension." + Fore.RESET + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(prog="MODULA 0.1", description="Generate modulated audio tones and phone ring tones")
    parser.add_argument('-dest', '--destination', type=check_extension, default="modulated_audio_signal.wav", help="Destination file name")
    parser.add_argument('-dur', '--duration', type=int, default=2, help="Audio duration, in seconds (ignored in ring mode)")
    parser.add_argument('-sr', '--sample_rate', type=int, default=44100, help="Sample rate in Hz")
    parser.add_argument('-freq', '--frequency', type=int, default=440, help="Base frequency in Hz")
    parser.add_argument('-mr', '--modulation_rate', type=int, default=12, help="Modulation rate in Hz (ignored in ring mode)")
    parser.add_argument('-play', '--play_audio', action='store_true', help="Play modulated signal")
    parser.add_argument('-wr', '--write_data', action='store_true', help="Create text file with audio data")
    parser.add_argument('-sig', '--signal', default='sin', choices=['sin', 'sqrt', 'trg', 'swt'], help="Modulation wave (ignored in ring mode)")
    parser.add_argument('-scl', '--scale', default=32767, type=int, help="Sound scale")

    args = parser.parse_args()


if __name__ == '__main__':
    main()
