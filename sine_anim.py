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
    amplitude = 1
    frequency = 0.2
    length = 1000
    frames = 50

    plotext.title("Sine Animation")
    plotext.clc()

    for i in range(frames):
        plotext.clt()
        plotext.cld()

        x = np.linspace(0, 10, length)
        phase = 2 * np.pi * i / frames  # Variamos la fase en cada frame

        y = amplitude * np.sin(frequency * x + phase)
        
        plotext.plot(x, y, marker="dot", color="red")
        plotext.ylim(-1.0, 1.0)  # Limitamos el eje y a un rango fijo
        plotext.xlim(0, 10)      # Limitamos el eje x a un rango fijo
        plotext.sleep(0.1)
        plotext.show()

if __name__ == "__main__":
    main()
