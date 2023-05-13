#IMPORTAR LIBRERIA
import openai
import win32com.client as wc

# INTRODUCIR CLAVE
key = "<your_api_key>"
openai.api_key = key
speak=wc.Dispatch("Sapi.SpVoice")

# BUCLE
while True:
    
    # INTRODUCIR PREGUNTA A ENVIAR
    prompt = input("\nIntroduce pregunta: ")

    # CONDICIÓN PARA FINALIZAR BUCLE
    if prompt == "END":
        break

    # OBTENER RESPUESTA
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=2048)

    # MOSTAR RESPUESTA EN PANTALLA
    response = completion.choices[0].text
    print(response)
    speak.Speak(response)
