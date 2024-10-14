import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def bernstein(n, i, t):
    coeff = math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
    return coeff * (t ** i) * ((1 - t) ** (n - i))

def bezier_surface(control_points, u_steps=20, v_steps=20):
    n = len(control_points) - 1
    m = len(control_points[0]) - 1
    u = np.linspace(0, 1, u_steps)
    v = np.linspace(0, 1, v_steps)
    surface = np.zeros((u_steps, v_steps, 3))

    for i in range(n + 1):
        for j in range(m + 1):
            bern_u = bernstein(n, i, u)
            bern_v = bernstein(m, j, v)
            for k in range(u_steps):
                for l in range(v_steps):
                    surface[k, l] += bern_u[k] * bern_v[l] * control_points[i][j]

    return surface

control_points = np.array([
    [[0, 0, 0], [1, 0, 2], [2, 0, 0]],
    [[0, 1, 3], [1, 1, 4], [2, 1, 3]],
    [[0, 2, 0], [1, 2, 2], [2, 2, 0]]
])

surface = bezier_surface(control_points, u_steps=30, v_steps=30)

# Separar las coordenadas de la superficie
x = surface[:, :, 0]
y = surface[:, :, 1]
z = surface[:, :, 2]

# Crear la figura y el gráfico 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Dibujar la superficie
ax.plot_surface(x, y, z, color='skyblue', rstride=1, cstride=1, alpha=0.7, edgecolor='k')

# Dibujar los puntos de control
for row in control_points:
    ax.plot([p[0] for p in row], [p[1] for p in row], [p[2] for p in row], 'ro-')

# Configurar etiquetas y título
ax.set_title("Superficie de Bézier")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
