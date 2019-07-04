from VALID import OKI, ns
import time
import subprocess
parti=[0,0,0,0,0,0]
total=0
i=0

def resultado(p):
    if p in range(0,51):
        r=("INFRAVALORACIÓN")
    elif p in range(51,100):
        r=("VALORACIÓN ADECUADA")
    else:
        r=("SOBREVALORACIÓN")
    print("\nPUNTUACIÓN TOTAL: ",p)
    print(r)
        
def validate(p):
    global total
    global i
    global parti
    if i==6:
        i=0
    while not int(p) in range(0,5):
        p=OKI(input("INTRODUZCA VALOR ENTRE 0 Y 4: "))
    total+=p
    parti[i]+=p
    i+=1
    #print(parti)

        
while True:
    
    print("¿SABE VALORARSE?")
    print("""Este test permite medir la atuoestima...""")
    print("\n1)AL REDACTAR EL CURRÍCULUM VITAE PARA UN IMPORTANTE TRABAJO:")
    time.sleep(1)
    validate(OKI(input("\nA)Estoy seguro de poder afrontar el nuevo empleo: ")))
    validate(OKI(input("\nB)Describo adecuadamente mis límites y defectos: ")))
    validate(OKI(input("""\nC)Pongo de manifiesto mis capacidades para relacionarme
con los demás en ambientes nuevos: """)))
    validate(OKI(input("\nD)Muestro iniciativa al personalizar el currículum: ")))
    validate(OKI(input("\nE)Estoy dispuesto a aceptar los riesgos del nuevo trabajo: ")))
    validate(OKI(input("""\nF)Pienso que no me escojerán porque contratarán a alguien
con recomendaciones: """)))
    print("\n2)SE CITA EN UN RESTAURANTE CON UNA PERSONA QUE LE GUSTA DESDE HACE TIEMPO:")
    time.sleep(1)
    validate(OKI(input("\nA)Estoy seguro que durante la velada me mostraré expontaneo: ")))
    validate(OKI(input("""\nB)Me pongo el traje con el que me siento más a gusto, aunque
esté pasado de moda: """)))
    validate(OKI(input("\nC)Estoy eufórico y le contagiaré mi estado de animo: ")))
    validate(OKI(input("\nD)Organizo una noche mas bién original: ")))
    validate(OKI(input("""\nE)Ya me siento satisfecho con el hecho de que haya
aceptado cenar conmigo: """)))
    validate(OKI(input("""\nF)El éxito de la velada no dependerá del restaurante sino
de mi capacidad para interesar al otro: """)))
    print("\n3)LA VÍSPERA DEL EXAMEN DE CONDUCIR:")
    time.sleep(1)
    validate(OKI(input("\nA)Me siento confiado en las enseñanzas de mi profesor de autoscuela: ")))
    validate(OKI(input("\nB)Les cuentos a mis amigos mis dificultades, por ejemplo, para aparcar: ")))
    validate(OKI(input("\nC)Comparto el estado de ánimo de los que se van a examinar conmigo: ")))
    validate(OKI(input("\nD)Ya he pensado el coche que voy a comprar: ")))
    validate(OKI(input("\nE)Pienso en los errores que cometí en las clases y como subsanarlos: ")))
    validate(OKI(input("""\nF)Estot convencido de que la suerte no tendrá nada que ver con el resultado
e la prueba: """)))
    print("\n4)SUS AMIGOS CRITICAN UNA DECISIÓN O POSTURA SUYA.")
    time.sleep(1)
    validate(OKI(input("\nA)Les planto cara y mantengo mi punto de vista: ")))
    validate(OKI(input("\nB)Medito las razones que les han llevado a criticar mi posición ")))
    validate(OKI(input("\nC)Acepto un acuerdo para mantener la unidad del grupo: ")))
    validate(OKI(input("\nD)Organizo una cena para hablar del tema: ")))
    validate(OKI(input("\nE)Asumo toda la responsabilidad de la decisión que he tomado: ")))
    validate(OKI(input("\nF)Mantengo mi postura a pesar de la disconformidad de la mayoría: ")))
    print("\n5)EN UN PARTIDO DE FUTBOL EN EL QUE EL EQUIPO SE LO JUEGA TODO, EL ENTRENADOR LE SELECCIONA COMO TITULAR")
    time.sleep(1)
    validate(OKI(input("\nA)Estoy convencido de que todo el equipo me apoyará: ")))
    validate(OKI(input("\nB)Le cuento al entrenador mis dudas y opiniones: ")))
    validate(OKI(input("\nC)Tenía el mismo sentimiento de compañerismo cuando era suplente: ")))
    validate(OKI(input("\nD)Creo que aseguraré mi puesto con este encuentro: ")))
    validate(OKI(input("\nE)Jugaré lo mejor que pueda: ")))
    validate(OKI(input("\nF)El resultado del partido no dependerá de las condiciones del campo: ")))

    resultado(total)
    print("\nPERFILES PARTICULARES:\n")
    print("SEGURIDAD: ",parti[0])
    print("IDENTIDAD: ",parti[1])
    print("PERTENENCIA: ",parti[2])
    print("VISIÓN DE FUTURO: ",parti[3])
    print("COMPETENCIA: ",parti[4])
    print("CONTROL: ",parti[5])

    conti=ns(input("¿Repetir test?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
