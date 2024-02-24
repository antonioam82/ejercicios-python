import numpy as np
from scipy.io import wavfile
from scipy.signal import sawtooth
import argparse
from playsound import playsound
from colorama import init, Fore, Style
import pyfiglet
import sounddevice as sd
import os

init()

signals = ["sin","sqrt","trg","swt"]

def write_data(name, signal, duration, sample_rate, frequency, modulation_rate, scale):
    with open(name.replace('.wav', '_data.txt'), 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Signal: {signal}\n")
        file.write(f"Duration: {duration} seconds\n")
        file.write(f"Sample Rate: {sample_rate} Hz\n")
        file.write(f"Frequency: {frequency} Hz\n")
        file.write(f"Modulation Rate: {modulation_rate} Hz\n")
        file.write(f"Scale: {scale}")

def play_audio(file_name):
    sample_rate, audio_data = wavfile.read(file_name)
    sd.play(audio_data, sample_rate)
    sd.wait()

def check_extension(file):
    name, ex = os.path.splitext(file)
    if ex == ".wav":
        return file
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + f"result file must have '.wav' extension." + Fore.RESET + Style.RESET_ALL)

def check_type(t):
    if t in signals:
        return t
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + "Ivalid signal type: Must be 'sin', 'sqrt', 'trg' or 'swt'." + Fore.RESET + Style.RESET_ALL)
    
def generate_tone(args):
    name = args.destination
    duration = args.duration
    sample_rate = args.sample_rate
    frequency = args.frequency
    modulation_rate = args.modulation_rate
    signal = args.signal
    scale = args.scale
    
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    if signal == "sin":
        modulation_wave = np.sin(2 * np.pi * frequency * t)
    elif signal == "sqrt":
        modulation_wave = np.sign(np.sin(2 * np.pi * 10 * t))
    elif signal == "trg":
        modulation_wave  = np.abs(sawtooth(2 * np.pi * 8 * t, width=0.5)) - 0.5  # 8 Hz
    elif signal == "swt":
        modulation_wave = sawtooth(2 * np.pi * 6 * t)

    #modulation_wave = np.sin(2 * np.pi * modulation_rate * t)
    modulated_wave = np.sin(2 * np.pi * (frequency + modulation_rate * modulation_wave) * t)
    modulated_wave /= np.max(np.abs(modulated_wave), axis=0)
    wavfile.write(name, sample_rate, np.int16(modulated_wave * scale))
    #wavfile.write(name, sample_rate, np.int16(modulated_wave * args.sample_rate))

    print("Modulated signal audio saved correctly.")
    if args.play_audio:
        print(f"\nPlaying '{name}'")
        play_audio(name)

    if args.write_data:
        write_data(name, signal, duration, sample_rate, frequency, modulation_rate, scale)
        print(f'Created data file "{args.destination}", correctly')

def main():
    parser = argparse.ArgumentParser(prog="MODULA 0.1",description="Generate modulated audio tones")
    parser.add_argument('-dest','--destination',type=check_extension,default="modulated_audio_signal.wav",help="Destination file name")
    parser.add_argument('-dur','--duration',type=int,default=3,help="Audio duration, in seconds")
    parser.add_argument('-sr','--sample_rate',type=int,default=44100,help="Sample rate in Hz")
    parser.add_argument('-freq','--frequency',type=int,default=440,help="Base frequency in Hz")
    parser.add_argument('-mr','--modulation_rate',type=int,default=12,help="Modulation rate in Hz")
    parser.add_argument('-play','--play_audio',action='store_true',help="Play modulated signal")
    parser.add_argument('-wr','--write_data',action='store_true',help="Create text file with audio data")
    parser.add_argument('-sig','--signal',default='sin',type=check_type,help="Modulation wave")
    parser.add_argument('-scl','--scale',default=32767,type=int,help="Sound scale")
    
    args = parser.parse_args()
    try:
        print(pyfiglet.figlet_format("modula",font="larry3d"))
        generate_tone(args)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + "\nUNEXPECTED ERROR: ",str(e) + Fore.RESET + Style.RESET_ALL)

if __name__ == '__main__':
    main()
