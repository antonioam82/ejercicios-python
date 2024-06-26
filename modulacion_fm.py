import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
from math import pi
import pylab as pl
from math import log10

plt.close('all')

Vm= float(input("Amplitud de la Moduladora: "))
Fm= float(input("Frecuancia de la Moduladora: "))
Vc= float(input("Amplitud de la Portadora: "))
Fc= float(input("Frecuencia de la Portadora: "))
kf= float(input("Factor de sensibilidad de frecuencia: "))
n= float(input("Numero de periodos: "))
print("")

z = 50
Af = kf*Vm
B = Af/Fm

Fs = 50000 # Frecuencia de muestreo
x = 0
n0 = [] 
bessel = []
f = np.arange(0,10,1)

# ECUACIONES PARA HALLAR BESSEL
for i in range(0,len(f)):
    x = round(sp.jv(i,B),2)
    bessel.append(x)

n_positivos = bessel[1:11];
n_negativos = np.flip(n_positivos);
n0.append(bessel[0]);

jn = np.concatenate((n_negativos,n0,n_positivos))

nB = 4
Bwb = 2*Fm*nB
BWc = 2*(Af*Vm)


f_ns = []
f_ps = []
F0 = []
F0.append(Fc)

for f_inicial in range(0,len(f)):

    if f_inicial == 0:
        f_1=Fc-Fm;
        f_inicial=f_1;

    else:
        f_1 = f_1-Fm;
        f_inicial=f_1;

    f_ns.append(f_inicial);

finv_ns = np.flip(f_ns);

for f_final in range(0,len(f)):

    if f_final==0:
        f_1=Fc+Fm;
        f_final = f_1;

    else:
        f_1=f_1+Fm;
        f_final = f_1;

    f_ps.append(f_final);
f_inv_ps = np.flip(f_ps);
Fn = np.concatenate((finv_ns,F0,f_ps))

t = np.arange(0,n*1/Fm,1/Fs)

f_VcJn = []
VcJn = 0
VcJn = np.round(abs((jn*Vc)/(np.sqrt(2))),2)
f_VcJn.append(VcJn)

f_VndB = []
VndB = 0
VndB = np.round(abs((20*np.log10(VcJn))),2)
f_VndB.append(VndB)


f_PnW = []
PnW = 0
PnW = abs(((jn*Vc)**2)/100)
f_PnW.append(PnW)

f_PndBm = []
PndBm = 0
PndBm = np.round(abs((10*np.log10(PnW*1000))),2)
f_PndBm.append(PndBm)


Vportadora = Vc*np.cos(2*pi*Fc*t)
Vmoduladora = Vm*np.sin(2*pi*Fm*t)
Vfm = Vc*np.cos(2*pi*Fc*t+B*np.sin(2*pi*Fm*t))

print('RESULTADOS MODULACIÓN FM\n')
print('{:^10} {:^10} {:^10} {:^10}'.format('Af','B','BWd','Bwc'))
print('{:^10} {:^10} {:^10} {:^10}'.format(Af,B,Bwb,BWc))
print("")
print('{:^10} {:^9} {:^9} {:^9} {:^9}'.format('Jn','Fn','Vc*Jn','Vn(dB)','Vn(dBm)'))
for formatted in map('{:^10} {:^10} {:^9} {:^10} {:^10}'.format, jn, Fn, VcJn, VndB, PndBm):
    print(formatted)

print("\nECUACION PORTADORA:")
print("Vc(t)=",Vc,"cos(2pi",Fc,"t)")
print("\nECUACION MODULADORA:")
print("Vm(t)=",Vm,"sen(2pi",Fm,"t)")
print("\nECUACION GENERAL PARA FM:")
print("Vfm(t)=",Vc,"cos[2pi",Fc,"t +", B, "sen(2pi",Fm,"t)]")

fig = plt.figure()
fig,plt.subplot(1,1,1)
plt.plot(t,Vportadora,color="blue",linewidth=0.8)
plt.title("Señal Portadora")
plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.grid(True)

fig1 = plt.figure()
fig1,plt.subplot(1,1,1)
plt.plot(t,Vmoduladora,color="black",linewidth=0.8)
plt.title("Señal Moduladora")
plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.grid(True)

fig2 = plt.figure()
fig2,plt.subplot(1,1,1)
plt.plot(t,Vfm,color="red",linewidth=0.8)
plt.title("Modulacion de Frecuecia")
plt.xlabel('tiempo')
plt.ylabel('amplitud')
plt.grid(True)

plt.show()
