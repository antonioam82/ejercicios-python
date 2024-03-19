import plotext
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(prog="CMD-SIN",description="Sine function simulations on CMD")
    parser.add_argument('-fms','--frames',type=int,default=100,help="Number of frames for the animation.")
    parser.add_argument('-amp','--amplitude',type=int,default=1,help="Amplitude for sine waves.")
    parser.add_argument('-per','--periods',type=int,default=4,help="Number of periods.")
    parser.add_argument('-freq','--frequency',type=float,default=1,help="Sine frequency value")
    parser.add_argument('-tm','--time',type=int,default=40,help="Sine time")
    
    args = parser.parse_args()
    sine_anim(args)

def sine_anim(args):
    amplitude = args.amplitude
    frequency = args.frequency
    length = 1000
    frames = args.frames

    plotext.title("Sine Animation")
    plotext.clc()

    for i in range(frames):
        plotext.clt()
        plotext.cld()

        x = np.linspace(0, 10, length)
        phase = 2 * np.pi * i / args.time #frames

        y = amplitude * np.sin(frequency * x + phase)

        plotext.plot(x, y, marker="dot", color="red")
        plotext.ylim(-1.0, 1.0)
        plotext.xlim(0, 10)
        plotext.sleep(0.01)
        plotext.show()

if __name__=='__main__':
    main()
