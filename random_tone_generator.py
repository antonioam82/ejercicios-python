import random
from pydub import AudioSegment
from pydub.generators import Sine, Square
from pydub.playback import play

# Crear una lista de frecuencias aleatorias
frequencies = [random.randint(100, 1000) for _ in range(10)]

# Generar segmentos de tonos aleatorios
sounds = []
for frequency in frequencies:
    duration = random.uniform(10.1, 20.5)  # Duración aleatoria entre 0.1 y 0.5 segundos
    #duration = random.uniform(100.1, 400.5)
    volume = random.uniform(0.1, 1.0)  # Volumen aleatorio entre 0.1 y 1.0
    tone = Sine(frequency).to_audio_segment(duration=duration)
    #tone = Square(frequency).to_audio_segment(duration=duration)
    tone = tone - random.randint(-30, 30)  # Aplicar variaciones de volumen
    sounds.append(tone)

# Combinar los segmentos de sonido aleatorios
combined_sound = sum(sounds)

# Reproducir el sonido combinado
play(combined_sound)
combined_sound.export("custom_tone.wav", format="wav") # Guardar tono como archivo 'wav'
