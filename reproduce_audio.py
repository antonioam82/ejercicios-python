import subprocess

def reproducir_mp3(ruta_archivo):
    # Comando para reproducir el archivo MP3 con ffmpeg
    comando = ['ffplay', '-nodisp', '-autoexit', ruta_archivo]

    # Ejecutar el comando en un proceso
    subprocess.call(comando)

# Ruta al archivo MP3
ruta_mp3 = "grabacion.mp3"

# Llamar a la función para reproducir el archivo MP3
reproducir_mp3(ruta_mp3)
