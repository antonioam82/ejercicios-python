#IMPORTAR "opencv2".
import cv2

#CARGAR IMAGEN
img = cv2.imread('Honda_goldwing_1500.jpg',0)

#MOSTRAR IMAGEN EN ESCALA DE GRISES.
cv2.imshow('image',img)
k = cv2.waitKey(0)

#CONTROL DE VENTANA POR TECLADO.
if k == 27: 
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Honda_goldwing_gray.jpg',img)
    cv2.destroyAllWindows()
