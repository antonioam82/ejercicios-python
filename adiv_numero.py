import random
import pickle
import subprocess

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def limites(n,MAX):
    while n<0 or n>MAX:
        n=OKI(input("ERROR: El número ha de estar entre 0 y"+str(" "+str(MAX)+": ")))
    return n

def sing_plu(f):
    if f>1:
        co=("intentos")
    else:
        co=("intento")
    return co

def paramar(n):
    m=n-1
    return m

while True:
    marca=pickle.load(open("mejor_marca","rb"))
    print("ADIVINA NUMERO-SUPER DESAFIO")
    print("""En este juego el usuario ha de adivinar un número,escogido
al azar por la computadora, dentro de un rango determinado.""")
    print("""ESCOJA EL NIVEL DE DIFICULTAD
NIVEL 1: ENTRE 0 Y 100
NIVEL 2: ENTRE 0 Y 1000
NIVEL 3: ENTRE 0 Y 10000
NIVEL 4: ENTRE 0 Y 100000""")
    level=OKI(input("Escriba aquí su opción (de 1 a 4): "))
    while level!=1 and level!=2 and level!=3 and level!=4:
        #PEDIMOS NIVEL DE DIFICULTAD
        level=OKI(input("Escriba un número comprendido entre 1 y 4: "))
        
    MAX=10**(level+1) #ESTABLECEMOS EL MAXIMO EN FUNCIÓN DEL NIVEL
    Di=(" 0 y "+str(MAX))
    numero_elegido=random.randint(0,MAX)#NÚMERO 'ESCOGIDO' POR LA COMPUTADORA
    print(numero_elegido)
    intentos=0 #CONTADOR DE INTENTOS
    #PRIMERA ELECCIÓN DE USUARIO (FUERA DE BUCLE).
    tu_numero=limites(OKI(input("Escribe un número comprendido entre"+Di+": ")),MAX)
    diferencia=abs(tu_numero-numero_elegido)#DISTANCIA CON EL NÚMERO 'ELEGIDO' POR LA COMPUTADORA
    num_anterior=tu_numero
    intentos+=1
    repes=1 #"repes" contabiliza el número de veces seguidas que se introduce un número.
    while tu_numero!=numero_elegido:
        #ULTERIORES ELECCIONES DE USUARIO (DENTRO DE BUCLE).
        tu_numero=(limites(OKI(input("Escribe un número comprendido entre"+Di+": ")),MAX))
        if abs(tu_numero-numero_elegido)>0:
            if tu_numero!=num_anterior:
                if (abs(tu_numero-numero_elegido))<diferencia:
                    print("TE ESTAS ACERCANDO")
                else:
                    print("TE ESTAS ALEJANDO")
            else:
                repes+=1
                print("HAS INTRODUCIDO EL MISMO NÚMERO",repes,"VECES SEGUIDAS")
        diferencia=abs(tu_numero-numero_elegido)            
        num_anterior=tu_numero   
        intentos+=1 #SE SUMA 1 POR CADA INTENTO
        if intentos==(MAX/2):#SI EL NÚMERO DE INTENTOS ES IGUAL A LA MITAD DE NÚMEROS, FIN DEL JUEGO.
            print(("PERDISTE: Superaste el límite de intentos permitido para este nivel("+str(int((MAX/2)))+" intentos)."),(chr(7)))
            print("La solución era",numero_elegido)
            break
    if tu_numero==numero_elegido:#SI EL USUARIO ACIERTA...
        print("¡BINGO!")
        print("Lo lograste en",intentos,sing_plu(intentos))
        posi_marca=paramar(level)
        if intentos<marca[posi_marca]:
            marca[posi_marca]=intentos
            pickle.dump(marca,open("mejor_marca","wb"))
            print("¡¡NUEVO RECORD!!")
        print("MEJOR MARCA PARA ESTE NIVEL: ",marca[posi_marca])
        if marca[posi_marca]==1:
            marca[posi_marca]=MAX
            pickle.dump(marca,open("mejor_marca","wb"))
    conti=ns(input("¿Jugar otra vez?: "))
    if conti==("n"):
        break
    try:
        subprocess.call(["cmd.exe","/C","cls"])
    except:
        continue
    
