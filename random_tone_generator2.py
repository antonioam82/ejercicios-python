from pydub import AudioSegment
from pydub.generators import Sine
import numpy as np
import os

os.chdir(r'C:\Users\Antonio\Documents\audios')

def generate_random_sound(duration=2000, num_tones=30, output_file="random_sound.wav"):
    """
    Genera un archivo de sonido aleatorio.
    
    :param duration: Duración total del sonido en milisegundos.
    :param num_tones: Número de tonos diferentes a generar.
    :param output_file: Nombre del archivo de salida.
    """
    # Duración de cada tono
    tone_duration = duration // num_tones

    # Crear una lista para almacenar los segmentos de audio
    audio_segments = []

    for _ in range(num_tones):
        # Generar una frecuencia aleatoria entre 100 Hz y 2000 Hz
        frequency = np.random.randint(100, 2000)
        
        # Generar un tono seno con la frecuencia aleatoria
        tone = Sine(frequency).to_audio_segment(duration=tone_duration)
        
        # Agregar el tono a la lista de segmentos de audio
        audio_segments.append(tone)

    # Concatenar todos los segmentos de audio en un solo segmento
    combined_audio = sum(audio_segments)
    
    # Exportar el audio combinado a un archivo
    combined_audio.export(output_file, format="wav")
    print(f"Archivo de sonido generado: {output_file}")

# Ejecutar la función para generar el sonido aleatorio
generate_random_sound()
