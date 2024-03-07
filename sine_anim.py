'''import plotext
import numpy as np

def main():
    l = 1000
    frames = 50

    plotext.title("Sine Animation")
    plotext.clc()

    for i in range(frames):
        plotext.clt()
        plotext.cld()

        x = np.linspace(0, 10, l)
        y = np.sin(1 * x + 2 * np.pi * i / frames)
        
        plotext.xlim(0, 10)
        plotext.plot(x, y, marker="dot", color="red")
        plotext.sleep(0.1)
        plotext.show()

if __name__ == "__main__":
    main()'''

####################################################

import plotext
import numpy as np

def main():
    l = 10
    frames = 50

    plotext.title("Sine Animation")
    plotext.clc()

    for i in range(frames):
        plotext.clt()
        plotext.cld()

        x = np.linspace(0, 10, l)

        # Ajustar la frecuencia, fase y amplitud
        frequency = 1#0.3  # Frecuencia original
        phase = 0  # Fase original
        amplitude = 1  # Amplitud original

        y = amplitude * np.sin(frequency * x + 2 * np.pi * i / frames + phase)
        
        plotext.xlim(0, 10)
        plotext.plot(x, y, marker="dot", color="red")
        plotext.sleep(0.05)
        plotext.show()

if __name__ == "__main__":
    main()
