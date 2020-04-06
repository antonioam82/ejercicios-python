import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint

fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')

ax.azim = 45
ax.elev = 45

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

ax.set_xticklabels("")
ax.set_yticklabels("")
ax.set_zticklabels("")

linea, = ax.plot([],[],[],label = 'Lorenz', lw = 0.5)
ax.legend()

ax.set_xlim(-20.20)
ax.set_ylim(-30,30)
ax.set_zlim(0,50)

def integra(ccii,t):
    x = ccii[0]
    y = ccii[1]
    z = ccii[2]
    sigma = 10
    rho = 28
    beta = 8.0/3
    dx = sigma*(y-x)
    dy = x*(rho-z)
    dz = x*y-beta*z
    return [dx,dy,dz]

def anima(i,x0,y0,z0):
    t = np.arange(0,(i+1)/10.,0.01)
    ccii = [x0,y0,z0]
    soluc = odeint(integra,ccii,t)
    x = soluc[:,0]
    y = soluc[:,1]
    z = soluc[:,2]
    ax.elev = 45+i/2
    ax.azim = 45+i/2
    linea.set_data(x,y)
    linea.set_3d_properties(z)
    return linea 

anim = animation.FuncAnimation(fig,anima,frames=500,fargs=(0,1,1.05),
                               interval=5)
try:
    anim.save('Atractor_de_Lorenz(pybonacci).mp4', fps = 10)
except:
    print("Va ser que no")
