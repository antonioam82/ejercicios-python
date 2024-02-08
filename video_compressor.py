import cv2

def reducir_tamano_video(input_path, output_path, calidad_compresion):
    # Abrir el video de entrada
    cap = cv2.VideoCapture(input_path)

    # Obtener información del video original
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Definir el codec y crear el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Escribir el fotograma en el archivo de salida con la calidad de compresión especificada
        out.write(frame)

    # Liberar los recursos
    cap.release()
    out.release()

# Ruta del archivo de video de entrada y salida
input_path = 'video_original.avi'
output_path = 'video_reducido.avi'

# Calidad de compresión (rango de 0 a 100, donde 0 significa la compresión máxima)
calidad_compresion = 50  # Puedes ajustar este valor según tus necesidades

# Reducir el tamaño del video
reducir_tamano_video(input_path, output_path, calidad_compresion)

print("Video reducido generado exitosamente.")
