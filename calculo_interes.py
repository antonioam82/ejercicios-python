# -*- coding: utf-8 -*-
from VALID import ns #OK
import subprocess
 
def entradaNumero(texto, tipo):
    numero = -1
    while numero < 0:
        try:
            if tipo=="float":
                numero = float(input(texto))
            else:
                numero = int(input(texto))
        except:
            print("\tError, no es un valor correcto")
    return numero

while True:
    cantidad=entradaNumero("Indica la cantidad: ", "float")
    interes=entradaNumero("Indica el interes: ", "float")
    anos=entradaNumero("Indica los años: ", "int")
 
    print("\n--------------------------------------------------")
    for i in range(anos):
        print("año {0} capital {1:.2f} interes {2:.2f} total {3:.2f}".format(i+1, cantidad, cantidad*interes/100, cantidad + cantidad*interes/100))
        cantidad+=cantidad*(interes/100)
    conti = ns(input("\n¿Desea continuar?(n/s): "))
    if conti == "n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
