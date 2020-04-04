#!/usr/bin/python3
from VALID import ns, OK

print("\n--------------------LEY DE COLOUMB-------------------")
print("----------------Formula  F=K*(Q*Q'/d*d)--------------\n")

while True:
    c1 = OK(input("Digite carga1 Q  : "))
    c2 = OK(input("Digite carga2 Q' : "))
    d = OK(input("Digite distancia entre las cargas d: "))
    k=9000000000
    f=k*(c1*c2/d*d)
 
    print("La Fuerza de Atraccion o repulsion F es ",f,"Newtons")

    conti = ns(input("¿Desea continuar?(n/s): "))
    if conti == "n":
        break
