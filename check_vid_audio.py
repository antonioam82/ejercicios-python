from moviepy.editor import VideoFileClip

def video_contains_audio(file_path):
    try:
        video_clip = VideoFileClip(file_path)
        audio = video_clip.audio
        return audio
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Ruta al archivo de video que deseas verificar
video_path = file-path

audio_info = video_contains_audio(video_path)

if audio_info:
    print("El video contiene audio.")
    print("Información del audio:")
    print(f"Duración: {audio_info.duration} segundos")
    print(f"Frecuencia de muestreo: {audio_info.fps} Hz")
    print(f"Número de canales: {audio_info.nchannels}")
else:
    print("El video no contiene audio.")
