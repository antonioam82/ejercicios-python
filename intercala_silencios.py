from pydub import AudioSegment
from pydub.playback import play

# Cargar archivos de sonido
sound1 = AudioSegment.from_file("new_audio.wav", format="wav")
sound2 = AudioSegment.from_file("new_audio.wav", format="wav")
sound3 = AudioSegment.from_file("new_audio.wav", format="wav")

# Crear un segmento de silencio de 2 segundos
silence = AudioSegment.silent(duration=2000)  # 2000 ms = 2 segundos

# Concatenar sonidos intercalando silencios
combined = sound1 + silence + sound2 + silence + sound3 + silence

# Exportar el resultado a un nuevo archivo
combined.export("landline_phone_loop.wav", format="wav")

# (Opcional) Reproducir el resultado
#play(combined)
