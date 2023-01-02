import plotext
import numpy as np

'''X = np.random.random(100)
y = np.random.random(100)

plotext.scatter(X,y)
plotext.title("Random Data Points")
plotext.show()

plotext.clear_plot()

y = plotext.sin()
plotext.plot(y)
plotext.title("SIN")
plotext.show()

---------------------------------------

X = np.arange(0, 10, 0.1)
y = np.sin(X)
y2 = np.cos(X)

plotext.plot(X, y, label="Sin")
plotext.plot(X, y2, label="Cos")
plotext.title("Sin & Cos")
plotext.show()'''

############## sin function animation on cmd ################
l = 1000
x = range(1, l+1)
frames = 50

plotext.title("Sine Animation")
plotext.clc()

for i in range(frames):
    plotext.clt()
    plotext.cld()

    y = plotext.sin(1, 4, l, 2 * i / frames)
    plotext.xlim(0, 400)
    plotext.plot(x, y, marker="dot", color="red")
    plotext.sleep(0.001)
    plotext.show()

plotext.clear_plot()
