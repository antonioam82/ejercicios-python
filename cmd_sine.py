import plotext
import argparse
import numpy as np
from pynput import keyboard

stop = False

def main():
    parser = argparse.ArgumentParser(prog="CMD-SIN",description="Sine function simulations on CMD")
    #parser.add_argument('-fms','--frames',type=int,default=100,help="Number of frames for the animation.")
    parser.add_argument('-amp','--amplitude',type=float,default=1,help="Amplitude for sine waves.")
    #parser.add_argument('-per','--periods',type=int,default=4,help="Number of periods.")
    parser.add_argument('-freq','--frequency',type=float,default=1,help="Sine frequency value")
    parser.add_argument('-tm','--time',type=int,default=40,help="Time elapsed in seconds")
    
    args = parser.parse_args()
    sine_anim(args)

def on_press(key):
    global stop
    if key == keyboard.Key.space:
        stop = True
        return False

def sine_anim(args):
    amplitude = args.amplitude
    frequency = args.frequency
    length = 1000
    #frames = args.frames
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    plotext.title("Sine Animation -PRESS SPACE BAR TO SCAPE-")
    plotext.clc()

    #for i in range(frames):
    i = 0
    while True:
        plotext.clt()
        plotext.cld()

        x = np.linspace(0, 10, length)
        phase = 2 * np.pi * i / args.time ###

        y = amplitude * np.sin(frequency * x + phase)

        plotext.plot(x, y, marker="dot", color="red")
        plotext.ylim(-amplitude,amplitude)
        plotext.xlim(0, 10)
        plotext.sleep(0.01)
        plotext.show()
        i += 1

        if stop == True:
            print("Animation interrupted by user")
            break

if __name__=='__main__':
    main()

