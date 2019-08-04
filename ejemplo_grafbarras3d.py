#IMPORTAMOS MÓDULOS NECESARIOS.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#CREAMOS FIGURA.
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

#COORDENADA DE CADA BARRA
x = [1,2,3,4,2,6,7,8,9,10]
y = [3,4,6,7,1,2,5,9,10,5]
z = np.zeros(10)

dx = np.ones(10) #ANCHURA DE CADA BARRA
dy = np.ones(10) #PROFUNDIDAD DE CADA BARRA
dz = [2,3,4,3,4,5,3,7,8,2] #ALTURA DE CADA BARRA

#REPRESENTACION DE LOS DATOS
ax1.bar3d(x, y, z, dx, dy, dz)

plt.show()
