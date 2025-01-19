import pyttsx3

# Inicializar el motor de pyttsx3
engine = pyttsx3.init()

# Establecer el idioma (si es compatible con tu sistema)
engine.setProperty('voice', 'spanish')  # Algunas configuraciones pueden necesitar ajuste según el sistema
engine.setProperty('rate',200)

while True:
    texto = input("> ")
    engine.say(texto)
    engine.runAndWait()

    if texto == "":
        print("Programa terminado")
        break
    
