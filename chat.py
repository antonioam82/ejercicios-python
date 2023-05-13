#IMPORTAR LIBRERIA
import openai
import time
import os
import sys
from colorama import Fore, init

init()

# INTRODUCIR CLAVE
key = "<YOUR_API_KEY>"
openai.api_key = key

def typewriter(message):
    print(Fore.GREEN)
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
    print(Fore.RESET)

# BUCLE
while True:
    
    # INTRODUCIR PREGUNTA A ENVIAR
    prompt = input("\nPROMPT> ")

    # CONDICIÓN PARA FINALIZAR BUCLE
    if prompt == "END":
        break

    # OBTENER RESPUESTA
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=2048)

    # MOSTAR RESPUESTA EN PANTALLA
    response = str(completion.choices[0].text)
    
    typewriter(response)
    print("")
