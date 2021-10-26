#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from colorama import init, Fore, Back

def AB():
    while True:
        op = input("Introduzca aquí su opción: ").upper()
        if op == "A" or op == "B":
            return op
            break
        else:
            print("Introduce A o B según su opción.")

def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))
			
def change_dir():
    while True:
        dire = input("Introduzca directorio base: ")
        if os.path.isdir(dire):
            os.chdir(dire)
            break
        else:
            print("ERROR, DIRECTORIO NO VÁLIDO")

def ns(c):
    while c.lower()!=("s") and c.lower()!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c.lower())
	
while True:
    init()
    print(Back.BLUE+"\n----------------------------------FILE FINDER-----------------------------------")
    print(Back.RESET+"")
    print("Directorio actual: {} ".format(os.getcwd()))
    print("\n**********ELIJA OPCIÓN**********")
    print("A) BUSCAR ARCHIVOS POR EXTENSIÓN.")
    print("B) BUSCAR UN ARCHIVO POR NOMBRE.")
    print("********************************\n")
    count = 0
    opc = AB()
	
    if opc == 'A':
        change_dir()
        filetype = input("Introduce extension: ")
        print("BUSCANDO...\n")
        for nombredir, dirs, ficheros in os.walk(os.getcwd()):
            for nombrefichero in ficheros:
                if nombrefichero.endswith(filetype):
                    count+=1
                    print(Fore.GREEN+'{}-'.format(count)+os.path.join(nombredir,BMP(nombrefichero)))
                    
        print(Fore.BLACK+Back.GREEN+'\n{} ARCHIVOS ENCONTRADOS.'.format(count))
        print(Fore.RESET+Back.RESET+"")
					
    elif opc == "B":
        change_dir()
        texto_requerido = BMP(input("Introduce archivo a buscar o término de busqueda: "))##############
        print("BUSCANDO...\n")
        for root, folders, files in os.walk(os.getcwd()):
            for file in files:
                name,ex = os.path.splitext(file)
                if file.endswith(texto_requerido) or texto_requerido in name:
                    count+=1
                    print(Fore.GREEN+'{}-'.format(count)+os.path.join(root,BMP(file)))
            
        if count == 0:
            print(Fore.BLACK+Back.RED+"No se encontraron coincidencias con \'{}\'.".format(texto_requerido))
        else:
            print(Fore.BLACK+Back.GREEN+"\n{} ARCHIVOS ENCONTRADOS.".format(count))
        print(Fore.RESET+Back.RESET+"")
            
    conti = ns(input("¿Continuar(n/s)?: "))
    if conti == "n":
        break
