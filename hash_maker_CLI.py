import hashlib
from colorama import Fore, Back, init

# GENERAR CADENAS HASH A PARTIRDE TEXTO USANDO DIFERENTES ALGORITMOS

class HASH:
    def generateHash(h):
        digest=h.hexdigest()
        return digest
x = 0
init()
algoritmos = ["md5","sha1","sha224","sha256","sha384","sha512"]

print(Back.BLUE+"-"*56+"HASH CLI"+"-"*56+Back.RESET)
while x<1:
    print(Fore.GREEN+"Elija número de opción deseada:")
    print("1-Usar algoritmo MD5")
    print("2-Usar algoritmo SHA1")
    print("3-Usar algoritmo SHA224")
    print("4-Usar algoritmo SHA256")
    print("5-Usar algoritmo SHA384")
    print("6-Usar algoritmo SHA512")
    print("7-Finalizar programa")
    nAlgoritmo=int(input("Introducir opción: "))

    

    algoritmo = ""
    if nAlgoritmo != 7:

        datos=input("Introducir información a hashear: ")


        algoritmo = algoritmos[nAlgoritmo-1]
            
        bdatos = bytes(datos, 'utf-8')
        h = hashlib.new(algoritmo,bdatos)
        hash1=HASH.generateHash(h)
        print(""+Fore.YELLOW)
        print(hash1)
        print(""+Fore.RESET)
        x=0
    else:
        x=1
print("PROGRAM FINISHED")
