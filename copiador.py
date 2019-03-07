#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shutil import copyfile
from sys import exit

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)


origen = input("Introduce ruta del archivo a copiar: ")
destino = input("Introduce ruta de la carpeta de destino: ")

try:
    copyfile(origen, destino)
except IOError as e:
    print("No se pudo copiar el archivo. %s" % e)
    exit(1)
except:
    print("Error:", sys.exc_info())
    exit(1)

print("\nCopia realizada con exito\n")

while True:
    comprobar=ns(input("Desea visualizar el archivo copiado?: "))
    if comprobar ==("n"):
        break
    elif comprobar == 's':
        archivo = open(origen, "r")
        print("\nContenido:\n")
        print(archivo.read())
        archivo.close()
        print()
        break
    else:
        continue
