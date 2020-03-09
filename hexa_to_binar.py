#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

#CORRESPONDENCIA HEXADECIMAL-BINARIO
dic_hex={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
        '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111'}

while True:
    print("****************CONVERSOR HEXADECIMAL-BINARIO****************\n")
    hexa=input("Introduce hexadecimal: ")

    binario=""

    for i in hexa:
        if i in dic_hex:
            binario=binario+dic_hex[i]
        else:
            print("El carater",i,"no es hexadecimal, por lo que ha sido ignorado.")

    
    print("\nTRADUCCIÓN BINARIA:",binario)

    conti=ns(input("\n¿Desea continuar?(n/s): "))
    if conti=="n":
        break
    
