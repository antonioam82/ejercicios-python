# IMPORTAR LIBRERIAS Y RECURSOS
import cv2
import matplotlib.pyplot as plt
import numpy as np

# FUNCIÓN PARA HISTOGRAMA
def show_hist(title,img):
    media_valores = np.mean(img) # MEDIA DE LAS INTENSIDADES
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.figure()
    plt.title(title)
    plt.xlabel('Intensidades')
    plt.ylabel('Pixels')
    plt.plot(hist)
    plt.axvline(x=media_valores, color="r", label="media")
    plt.legend()
    plt.xlim([0,256])
    plt.show()

# CARGAR IMAGEN Y CONVERTIRLA A ESCALA DE GRISES
image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# MOSTRAR IMAGEN
cv2.imshow("Original",gray)
cv2.waitKey(0)

# MOSTRAR HISTOGRAMA
show_hist('Original',gray)

# ECUALIZAR HISTOGRAMA
equalized = cv2.equalizeHist(gray)

# MOSTRAR IMAGEN RESULTADO
cv2.imshow("Equalized",equalized)
cv2.waitKey(0)

# HISTOGRAMA
show_hist('Equalized',equalized)

# ALGORITMO CLAHE
clip = 2.0 # UMBRAL LIMITE

tile = 8  # TAMAÑO CELDA

clahe = cv2.createCLAHE(clipLimit=clip,tileGridSize=(tile, tile))
equalized_new = clahe.apply(gray)

# MOSTRAR IMAGEN
cv2.imshow("Equaelized (CLAHE)",equalized_new)
cv2.waitKey(0)

# MOSTRAR HISTOGRAMA
show_hist('Equalized (CLAHE)',equalized_new)

cv2.destroyAllWindows()
