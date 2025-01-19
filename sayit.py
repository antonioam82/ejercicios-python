import pyttsx3
import pyfiglet

engine = pyttsx3.init()

engine.setProperty('voice', 'spanish') 
engine.setProperty('rate',200)

print(pyfiglet.figlet_format("SayIt!\n",font="dos_rebel"))

while True:
    texto = input("> ")
    engine.say(texto)
    engine.runAndWait()

    if texto == "":
        print("Program finished")
        break
