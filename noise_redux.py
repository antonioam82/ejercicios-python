import ffmpeg

input_video = 'input_video.mp4'
output_video = 'output_video6.mp4'

# Aplicar filtro de reducción de ruido
denoise_filter = "hqdn3d=6:7:6:6"

# Comando de ffmpeg para aplicar el filtro de reducción de ruido
command = [
    'ffmpeg', '-i', input_video, '-vf', denoise_filter, '-c:a', 'copy', output_video
]

# Ejecutar el comando de ffmpeg
subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Reducción de ruido aplicada correctamente.")
