import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb  # Para calcular coeficientes binomiales de forma eficiente

# Definición de puntos de control
x = np.random.random_sample((3,))
y = np.random.random_sample((3,))
z = np.random.random_sample((3,))

CELLS = 10
nCPTS = len(x)  # Número de puntos de control
n = nCPTS - 1   # Número total de segmentos
t = np.linspace(0, 1, CELLS)  # Variable paramétrica
B = []

# Inicialización de las curvas de Bezier
xBezier = np.zeros(CELLS)
yBezier = np.zeros(CELLS)
zBezier = np.zeros(CELLS)

# Función que calcula el coeficiente binomial
def Ni(n, i):
    return comb(n, i)

# Función base de Bezier
def basisFunction(n, i, t):
    return Ni(n, i) * (t ** i) * (1 - t) ** (n - i)

# Cálculo de las curvas de Bezier
for k in range(nCPTS):
    B_k = basisFunction(n, k, t)
    B.append(B_k)

    xBezier += B_k * x[k]
    yBezier += B_k * y[k]
    zBezier += B_k * z[k]

# Gráfica en 3D
fig1 = plt.figure(figsize=(4, 4))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.scatter(x, y, z, c='black', label="Puntos de control")
ax1.plot(xBezier, yBezier, zBezier, c='blue', label="Curva de Bezier")

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

plt.legend()
plt.show()
