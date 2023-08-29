#import os
import cv2
import numpy as np
from scipy.linalg import svd

imagen = cv2.imread('portrait.jpg')

m,n = imagen.shape[:2]

cant_bytes_original = m*n*3

print(cant_bytes_original)

name = 'Imagen original (' + str(cant_bytes_original) + ' bytes)'

cv2.imshow(name, imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

B,G,R = cv2.split(imagen)
print(B)

U_B, s_B, V_transp_B = svd(B, full_matrices=False)
U_G, s_G, V_transp_G = svd(G, full_matrices=False)
U_R, s_R, V_transp_R = svd(R, full_matrices=False)

sigma_s_B = []
for i in range(len(s_B)):
    a = (s_B[i]/(sum(s_B)))*100
    sigma_s_B.append(a)
    
sigma_s_G = []
for i in range(len(s_G)):
    a = (s_G[i]/(sum(s_G)))*100
    sigma_s_G.append(a)

sigma_s_R = []
for i in range(len(s_R)):
    a = (s_R[i]/(sum(s_R)))*100
    sigma_s_R.append(a)

k = 12

U_B_k = U_B[:,:k]
Sigma_B_k = np.diag(s_B[:k])
V_transp_B_k = V_transp_B[:k,:]

U_G_k = U_G[:,:k]
Sigma_G_k = np.diag(s_G[:k])
V_transp_G_k = V_transp_G[:k,:]

U_R_k = U_R[:,:k]
Sigma_R_k = np.diag(s_R[:k])
V_transp_R_k = V_transp_R[:k,:]

B_reducida = U_B_k.dot(Sigma_B_k.dot(V_transp_B_k))
G_reducida = U_G_k.dot(Sigma_G_k.dot(V_transp_G_k))
R_reducida = U_R_k.dot(Sigma_R_k.dot(V_transp_R_k))

Imagen_SVD = np.zeros((m,n,3), dtype='uint8')

Imagen_SVD[:,:,0] = B_reducida
Imagen_SVD[:,:,1] = G_reducida
Imagen_SVD[:,:,2] = R_reducida

Imagen_con_SVD = cv2.merge([Imagen_SVD[:,:,0],Imagen_SVD[:,:,1],Imagen_SVD[:,:,2]])

img_original_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
img_reducida_grises = cv2.cvtColor(Imagen_con_SVD, cv2.COLOR_BGR2GRAY)

diferencia = img_original_grises - img_reducida_grises
mse = np.mean(diferencia**2)
print("ERROR CUADRÁTICO MEDIO: ",mse)

cant_bytes_reducida = m*k*3
print("CANTIDAD DE BYTES REQUERIDOS: ",cant_bytes_reducida)

tasa_compresion = cant_bytes_original / cant_bytes_reducida
print("TASA DE COMPRESION: ",tasa_compresion)

name = 'New'

cv2.imshow(name, Imagen_con_SVD)
cv2.waitKey(0)
cv2.destroyAllWindows()
