from VALID import ns,OKI
import subprocess

termi=["T","R","W","A","G","M","Y","F","P","D","X",
       "B","N","J","Z","S","Q","V","H","L","C","K","E"]

while True:
    num=OKI(input("Introduzca número: "))
    indice=num%23
    print("Letra: ",termi[indice])
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
        
    
