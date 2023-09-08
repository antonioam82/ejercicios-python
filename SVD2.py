#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from scipy.linalg import svd
import argparse
from colorama import init, Fore, Style
import os

init()

image_formats = ['.png','.jpg']

def calculate_metrics(i):
    img_original_grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_reducida_grises = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    diference = img_original_grises - img_reducida_grises
    print("")
    print(Fore.GREEN+"*************************REDUCTION DATA*************************")
    mse = np.mean(diference**2)
    print("Error cuadrático medio:                  ",mse)

    num_bytes_redux = m*byt*3
    #text = get_size_format(num_bytes_redux)
    print("Cantidad de bytes requeridos:            ",num_bytes_redux)

    tasa_compresion = num_bytes / num_bytes_redux
    print("Tasa de compresión:                      ",tasa_compresion)

    porcentag_reduccion = round((1 - num_bytes_redux / num_bytes)*100,2)
    print("Porcentage reducción de dimensionalidad: ",str(porcentag_reduccion)+'%')
    print("****************************************************************\n"+Fore.RESET)


def check_extension(file):
    #global ex
    name, ex = os.path.splitext(file)
    if ex in image_formats:
        return file
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + f"result file must be a supported image format ('.png' or '.jpg')." + Fore.RESET + Style.RESET_ALL)

def get_size_format(b, factor=1024, suffix="B"):
	for unit in ["","K","M","G","T","P","E","Z"]:
	    if b < factor:
	        return f"{b:.4f}{unit}{suffix}"
	    b /= factor
	return f"{b:.4f}Y{suffix}"

def check_value(v):
    if v.isdigit():
        v = int(v)
        if v > 0:
            return v
        else:
            raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + "Value must be bigger than 0" + Fore.RESET + Style.RESET_ALL)
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + "Value must be an integer" + Fore.RESET + Style.RESET_ALL)

def check_file(file):
    if file in os.listdir():
        name, ex = os.path.splitext(file)
        
        if ex in image_formats:
            return file
        else:
            raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + f"source file must be a supported image format ('.png' or '.jpg')." + Fore.RESET + Style.RESET_ALL)
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + f"file '{file}' not found." + Fore.RESET + Style.RESET_ALL)

def redux(args):
    global num_bytes, image, byt, m
    image = cv2.imread(args.source)
    byt = args.signif_bytes
    m,n = image.shape[:2]
    num_bytes = m*n*3
    print(Fore.YELLOW + Style.DIM + f"Number of bytes (source): {num_bytes}" + Fore.RESET + Style.RESET_ALL)
    B,G,R = cv2.split(image)
    svd_f(B,G,R,args.signif_bytes,m,n,args.destination)

def svd_f(B,G,R,k,m,n,nm):
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

    calculate_metrics(Imagen_con_SVD)
    cv2.imwrite(nm,Imagen_con_SVD)
    print(Fore.YELLOW + Style.DIM + f"Saved as '{nm}'." + Fore.RESET + Style.RESET_ALL)
    show_image(Imagen_con_SVD,nm)

def show_image(i,n):
    cv2.imshow(n,i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main():
    parser = argparse.ArgumentParser(prog="SVD2",description="Programa para reducir la dimensiomalidad de una imagen.")
    parser.add_argument('-src', '--source', type=check_file, required=True, help='Imagen fuente')
    parser.add_argument('-dest', '--destination', default="output_image.png", type=check_extension, help='Imagen reducida')
    parser.add_argument('-sigb', '--signif_bytes',type=check_value, required=True, help='Número de bytes significativos para apliación de reducción')

    args = parser.parse_args()
    redux(args)

if __name__ == "__main__":
    main()
