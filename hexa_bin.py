#CONVERSOR HEXADECIMAL-BINARIO (MÉTODO LARGO)
import subprocess

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)


lista_hex=['0','1','2','3','4','5','6','7'
           ,'8','9','A','B','C','D','E','F']

while True:
    print("****************TRADUCTOR HEXADECIMAL-BINARIO****************")
    print("")
    hexa=input("Introduce hexadecimal: ")

    binario=[]

    for i in hexa:
        if i in lista_hex:
            indice=lista_hex.index(i)
            num_binar=(bin(indice)).lstrip("0b")
            longi=(abs(len(num_binar)-4))
            n='0'*longi
            n_cadena=n+num_binar
            binario.append(n_cadena)
        else:
            print("El carater",i,"no es hexadecimal, por lo que ha sido ignorado.")

    binario_final=str(("").join(binario))
    
    print("")
    print("TRADUCCIÓN BINARIA:",binario_final)
    print("")

    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
    
