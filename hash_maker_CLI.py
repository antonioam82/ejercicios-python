#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from colorama import Fore, Back, init

class HASH:
    def generateHash(h):
        digest=h.hexdigest()
        return digest
    
init()
algoritmos = ["md5","sha1","sha224","sha256","sha384","sha512"]

print(Back.BLUE+"-"*56+"HASH CLI"+"-"*56+Back.RESET)
while True:
    print(Fore.GREEN+"Elija número de opción deseada:")
    print("1-Genererar hash usando algoritmo MD5")
    print("2-Genererar hash usando algoritmo SHA1")
    print("3-Genererar hash usando algoritmo SHA224")
    print("4-Genererar hash usando algoritmo SHA256")
    print("5-Genererar hash usando algoritmo SHA384")
    print("6-Genererar hash usando algoritmo SHA512")
    print("7-Finalizar programa.")

    try:
        nAlgoritmo = int(input("Introducir opción: "))

        if nAlgoritmo > 0 and nAlgoritmo < 8:

            if nAlgoritmo != 7:
                datos=input("Introducir información a hashear: ")
                algoritmo = algoritmos[nAlgoritmo-1]
                bdatos = bytes(datos, 'utf-8')
                h = hashlib.new(algoritmo,bdatos)
                hash1=HASH.generateHash(h)
                print(Fore.BLUE+f"\nALGORITMO: {algoritmo.upper()}"+Fore.RESET)
                print(Fore.YELLOW+hash1+Fore.RESET+"\n")
            else:
                break
        else:
            print("\n"+Back.RED+Fore.BLACK+"VALOR FUERA DE RANGO."+Fore.RESET+Back.RESET+"\n")
            
    except Exception as e:
        print("\n"+Back.RED+Fore.BLACK+str(e)+Fore.RESET+Back.RESET+"\n")
        
print("PROGRAM FINISHED")
