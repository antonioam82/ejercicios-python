#CONVERSOR HEXADECIMAL-BINARIO (MÉTODO CORTO).
import subprocess

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)


dic_hex={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
        '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111'}

while True:
    print("****************TRADUCTOR HEXADECIMAL-BINARIO****************")
    print("")
    hexa=input("Introduce hexadecimal: ")

    binario=[]

    for i in hexa:
        if i in dic_hex:
            binario.append(dic_hex[i])
        else:
            print("El carater",i,"no es hexadecimal, por lo que ha sido ignorado.")

    binario_final=("").join(binario)
    
    print("")
    print("TRADUCCIÓN BINARIA:",binario_final)
    print("")

    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
    
