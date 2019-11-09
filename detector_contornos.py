import cv2
import matplotlib.pyplot as plt

# LEER IMAGEN
image = cv2.imread(imagen)
# CONVERTIR A 'RGB'
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# CONVERTIR A ESCALA DE GRISES
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# IMAGEN BINARIA
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# MOSTRAR
plt.imshow(binary, cmap="gray")
plt.show()
# DETECTAR CONTORNOS EN IMAHEN BINARIA
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# DIBUJAR CONTORNOS
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# MOSTRAR CONTORNOS SOBRE LA IMAGEN ORIGINAL
plt.imshow(image)
plt.show()
