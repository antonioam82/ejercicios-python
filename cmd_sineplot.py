import plotext
import argparse

def main():

    parser = argparse.ArgumentParser(prog="CMD-SIN",description="Sine function simulations on CMD")
    parser.add_argument('-fms','--frames',type=int,default=100,help="Number of frames for the animation.")
    parser.add_argument('-amp','--amplitude',type=int,default=1,help="Amplitude for sine waves.")
    parser.add_argument('-per','--periods',type=int,default=4,help="Number of periods.")
    parser.add_argument('-pha','--phase',type=int,default=2,help="Phase.")

    args = parser.parse_args()
    sine_anim(args)

def sine_anim(args):
    l = 1000
    x = range(1, l+1)
    frames = args.frames

    plotext.title("Sine Animation")
    plotext.clc()
 
    for i in range(frames):
        plotext.clt()
        plotext.cld()

        y = plotext.sin(args.amplitude, args.periods, l, args.phase * i / frames)
        plotext.xlim(0, 400)
        plotext.plot(x, y, marker="dot", color="red")
        plotext.sleep(0.001)
        plotext.show()

    plotext.clear_plot()

if __name__=='__main__':
    main()
