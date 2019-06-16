#!/usr/bin/env python
# -*- coding: utf-8 -*-
LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    mensaje=input("Mensaje: ")
    myKey="MINOMBREESANTONIOALFONSO"
    accion=input("Mode: ")

    if accion=='encriptar':
        traducido=cifrar_mensaje(myKey,mensaje)
    elif accion=='descifrar':
        traducido=descifrar_mensaje(myKey,mensaje)
    print(traducido)

def cifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'encriptar')

def descifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'descifrar')

def traductor_mensaje(clave,mensa,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=LETRAS.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)

if __name__ == '__main__':
    main()
