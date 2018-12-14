rt random
from VALID import ns, OKI
import subprocess

titulos=["TITULO PRELIMINAR","DE LOS DERECHOS Y DEBERES FUNDAMENTALES",
           "DE LA CORONA","DE LAS CORTES GENERALES","DEL GOBIERNO Y DE LA ADMINISTRACION",
           "DE LAS RELACIONES ENTRE EL GOBIERNO Y LAS CORTES GENERALES",
           "DEL PODER JUDICIAL","ECONOMIA Y HACIENDA","DE LA ORGANIZACION TERRITORIAL DEL ESTADO",
           "DEL TRIBUNAL CONSTITUCIONAL","DE LA REFORMA CONSTITUCIONAL"]
                         
artics={"TITULO PRELIMINAR":(1,9),
        "DE LOS DERECHOS Y DEBERES FUNDAMENTALES":(10,55),"DE LA CORONA":(56,65),
        "DE LAS CORTES GENERALES":(66,96),"DEL GOBIERNO Y DE LA ADMINISTRACION":(97,107),
        "DE LAS RELACIONES ENTRE EL GOBIERNO Y LAS CORTES GENERALES":(108,116),
        "DEL PODER JUDICIAL":(117,127),"ECONOMIA Y HACIENDA":(128,136),
        "DE LA ORGANIZACION TERRITORIAL DEL ESTADO":(137,158),
        "DEL TRIBUNAL CONSTITUCIONAL":(159,165),"DE LA REFORMA CONSTITUCIONAL":(166,169)
        }

while True:
    usadas=[""]
    art_es=("")
    aciertos=0
    fallos=0
    print("TEST SOBRE LA ESTRUCTURA DE LA CONSTITUCIÓN ESPAÑOLA")
    print("""El usuario introducirá el nombre del título constitucional
en el que se encuentre el artículo indicado.""")
    num=OKI(input("Introduce el número de preguntas: "))
    print("")
    for i in range(num):
        while art_es in usadas: #PARA EVITAR REPETICIÓN DE ARTÍCULOS
            tit_selec=random.choice(titulos)
            art_es=random.randint((artics[tit_selec][0]),(artics[tit_selec][1]))
        print("Artículo",art_es)
        usadas.append(art_es)
        resp=input().upper()
        if resp==tit_selec:
            print("CORRECTO")
            aciertos+=1
        else:
            print("INCORRECTO")
            fallos+=1
        print("")
        if len(usadas)==170:
            usadas=[""]
            art_es=("")
    print("PUNTUACIÓN: ",(aciertos*10)/num)
    print(("%d preguntas,%d aciertos y %d fallos.")%(num,aciertos,fallos))
    ver=ns(input("¿Desea realizar un repaso del esquema de la Constitución Española?: "))
    if ver=="s":
        print("")
        print("***********************************************************************************")
        print("************************ESQUEMA DE LA CONSTITUCIÓN ESPAÑOLA************************")
        print("TÍTULO PRELIMINAR. (arts 1-9)")
        print("I)DE LOS DERECHOS Y DEBERES FUNDAMENTALES. (arts 10-55)")
        print("II)DE LA CORONA. (arts 56-65)")
        print("III)DE LAS CORTES GENERALES. (arts 66-96)")
        print("IV)DEL GOBIERNO Y DE LA ADMINISTRACIÓN. (arts 97-107)")
        print("V)DE LAS RELACIONES ENTRE EL GOBIERNO Y LAS CORTES GENERALES. (arts 108-116)")
        print("VI)DEL PODER JUDICIAL. (arts 117-127)")
        print("VII)ECONOMÍA Y HACIENDA. (arts 128-136)")
        print("VIII)DE LA ORGANIZACIÓN TERRITORIAL DEL ESTADO. (arts 137-158)")
        print("IX)DEL TRIBUNAL CONSTITUCIONAL. (arts 159-165)")
        print("X)DE LA REFORMA CONSTITUCIONAL. (arts 166-169)")
        print("***********************************************************************************")
        print("***********************************************************************************")
    print("")
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    try:
        subprocess.call(["cmd.exe","/C","cls"])
    except:
        continue
            
