# -*- coding: utf-8 -*-
from VALID import ns, OK, OKI
import subprocess

while True:
    print("\n---------------CALCULO DE INTERESES---------------")
    cantidad=OK(input("Indica la cantidad: "))
    interes=OK(input("Indica el interes: "))
    anos=OKI(input("Indica los años: "))
 
    print("\n--------------------------------------------------")
    for i in range(anos):
        print("año {0} capital {1:.2f} interes {2:.2f} total {3:.2f}".format(i+1, cantidad, cantidad*interes/100, cantidad + cantidad*interes/100))
        cantidad+=cantidad*(interes/100)
    conti = ns(input("\n¿Desea continuar?(n/s): "))
    if conti == "n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
