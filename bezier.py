import numpy as np
import matplotlib.pyplot as plt


x = np.random.random_sample((5,))
y = np.random.random_sample((5,))
z = np.random.random_sample((5,))

CELLS = 10
nCPTS = np.size(x, 0)
n = nCPTS - 1 # numero total de segmentos
i = 0
t = np.linspace(0, 1, CELLS) # VARIABLE PARAMETRICA
B = []

xBezier = np.zeros((1, CELLS))
yBezier = np.zeros((1, CELLS))
zBezier = np.zeros((1, CELLS))

def Ni(n, i):
    return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

def basisFunction(n, i, t):
    J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - i))
    return J

for k in range(0, nCPTS):
    B.append(basisFunction(n, i, t))

    xBezier = basisFunction(n, i, t) * x[k] + xBezier
    yBezier = basisFunction(n, i, t) * y[k] + yBezier
    zBezier = basisFunction(n, i, t) * z[k] + zBezier

    i += 1

'''for line in B:
    plt.plot(t, line)'''

fig1 = plt.figure(figsize=(4, 4))
ax1 = fig1.add_subplot(111,projection='3d')
ax1.scatter(x, y, z, c='black')
ax1.plot(xBezier[0], yBezier[0], zBezier[0], c='blue')

plt.show()
