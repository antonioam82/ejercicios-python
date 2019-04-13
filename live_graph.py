import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os

os.chdir(r'C:\Users\Antonio\Documents\docs')

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(111)

def animate(i):
    graph_data = open('ejemplo.txt','r').read()
    #count=0
    #for linea in graph_data:
        #count+=1
    #if count>1:
        #print(count)
    #else:
        #print("n")
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    #print("22")
       
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
           
