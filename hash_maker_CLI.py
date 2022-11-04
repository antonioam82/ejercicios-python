import hashlib
from colorama import Fore, init

class HASH:
    def generateHash(h):
        digest=h.hexdigest()
        return digest
x = 0
init()
while x<1:
    print(Fore.GREEN+"Elija número de opción deseada:")
    print("1-Usar algoritmo SHA256")
    print("2-Usar algoritmo SHA512")
    print("3-Finalizar programa")
    nAlgoritmo=int(input("Introducir opción: "))

    

    algoritmo = ""
    if nAlgoritmo != 3:

        datos=input("Introducir información a hashear: ")

        if nAlgoritmo == 1:
            algoritmo="sha256"
        else:
            algoritmo="sha512"
        #elif nAlgoritmo == 2:
            

        bdatos = bytes(datos, 'utf-8')
        h = hashlib.new(algoritmo,bdatos)
        hash1=HASH.generateHash(h)
        print(""+Fore.YELLOW)
        print(hash1)
        print(""+Fore.RESET)
        x=0
    else:
        x=1
print("THE END")
