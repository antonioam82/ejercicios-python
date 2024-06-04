import numpy as np
#from playsound import playsound
import sounddevice as sd
import argparse

def write_data(args):
    with open('signal_data.txt', 'w') as file:
        file.write(f"Modulating signal amplitude: {args.modulating_signal_amplitude}\n")
        file.write(f"Modulating signal frequency: {args.modulating_signal_frequency}\n")
        file.write(f"Carrier signal amplitude: {args.carrier_signal_amplitude}\n")
        file.write(f"Carrier signal frequency: {args.carrier_signal_frequency}\n")
        file.write(f"Modulation Index: {args.modulation_index}\n")
        file.write(f"Duration: {args.duration}\n")


def modulation_function(args):
    duration = args.duration
    A_m = args.modulating_signal_amplitude
    f_m = args.modulating_signal_frequency
    A_p = args.carrier_signal_amplitude
    f_p = args.carrier_signal_frequency
    ka = args.modulation_index
    
    t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
    mod = A_m*np.cos(2*np.pi*f_m*t)
    carr = A_p*np.cos(2*np.pi*f_p*t)
    AM_mod = A_p*(1+ka*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_p*t)

    return mod, carr, AM_mod

def main():
    parser = argparse.ArgumentParser(prog="MODULA_AM",conflict_handler='resolve',
                                     description="AM Modulation program")
    parser.add_argument('-csam','--carrier_signal_amplitude',required=True,type=float,help="Carrier signal amplitude value")
    parser.add_argument('-csfr','--carrier_signal_frequency',required=True,type=float,help="Carrier signal frequency value")
    parser.add_argument('-msam','--modulating_signal_amplitude',required=True,type=float,help="Modulating signal amplitude value")
    parser.add_argument('-msfr','--modulating_signal_frequency',required=True,type=float,help="Modulating signal frequency value")
    parser.add_argument('-mi','--modulation_index',required=True,type=float,help="Modulation index value")
    parser.add_argument('-dur','--duration',required=True,type=int,help="Signal duration in seconds")
    parser.add_argument('-wr','--write_data',action='store_true',help="Create text file with signal data")

    args = parser.parse_args()
    modulation, carrier, AM_modulated = modulation_function(args)

    if args.write_data:
        write_data(args)

    print('Playing Modulation Signal')
    sd.play(modulation, samplerate=44100)
    sd.wait()
    print("Playing Carrier Signal")
    sd.play(carrier, samplerate=44100)
    sd.wait()
    print("Playing AM Modulated")
    sd.play(AM_modulated, samplerate=44100)
    sd.wait()
    

if __name__=='__main__':
    main()
