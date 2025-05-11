import plotext
import argparse
import numpy as np
from pynput import keyboard
from colorama import init, Fore, Style

init()

stop = False
line_colors = ["red","green","blue"]

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

        plotext.plot(x, y, marker="braille", color=args.line_color)
        #plotext.grid(horizontal=True, vertical=True)
        plotext.ylim(-amplitude,amplitude)
        plotext.xlim(0, 10)
        plotext.sleep(0.01)
        plotext.show()
        i += 1

        if stop == True:
            print("Animation interrupted by user")
            listener.stop()
            break

def check_color(color):
    if color not in line_colors:
        raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+f"Color must be 'red', 'blue'or 'green'. {color} is not valid."+Fore.RESET+Style.RESET_ALL)
    return color
 

def main():
    parser = argparse.ArgumentParser(prog="CMD-SIN",description="Sine function simulations on CMD")
    #parser.add_argument('-fms','--frames',type=int,default=100,help="Number of frames for the animation.")
    parser.add_argument('-amp','--amplitude',type=float,default=1,help="Amplitude for sine waves.")
    #parser.add_argument('-per','--periods',type=int,default=4,help="Number of periods.")
    parser.add_argument('-freq','--frequency',type=float,default=1,help="Sine frequency value")
    parser.add_argument('-tm','--time',type=int,default=40,help="Time elapsed in seconds")
    parser.add_argument('-lc','--line_color',type=check_color,default="red",help="Line color")
    
    args = parser.parse_args()
    sine_anim(args)

if __name__=='__main__':
    main()
