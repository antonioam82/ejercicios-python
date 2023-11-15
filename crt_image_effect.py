import cv2
import numpy as np

def apply_crt_effect(image):
    # Cambiar el tamaño de la imagen para simular el efecto CRT
    resized = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    # Aplicar un efecto de desenfoque
    blur = cv2.GaussianBlur(resized, (5,5), 0)

    # Añadir efecto de distorsión con líneas horizontales y verticales
    num_iterations = 5
    for _ in range(num_iterations):
        for i in range(0, len(blur), 2):
            blur[i] = np.roll(blur[i], 1)

        for i in range(0, len(blur[0]), 2):
            blur[:, i] = np.roll(blur[:, i], 1)

    return blur

# Cargar la imagen
input_image = cv2.imread('source_image')

# Aplicar el efecto CRT
crt_effect = apply_crt_effect(input_image)
cv2.imwrite('effect_ima.jpg',crt_effect)

# Mostrar la imagen original y la imagen con efecto CRT
cv2.imshow('Original', input_image)
cv2.imshow('CRT Effect', crt_effect)
cv2.waitKey(0)
cv2.destroyAllWindows()
