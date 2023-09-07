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

def check_extension(file):
    #global ex
    name, ex = os.path.splitext(file)
    if ex in image_formats:
        return file
    else:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + f"result file must be a supported image format ('.png' or '.jpg')." + Fore.RESET + Style.RESET_ALL)

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
    global num_bytes
    image = cv2.imread(args.source)
    m,n = image.shape[:2]
    num_bytes = m*n*3
    print("Number of bytes: ",num_bytes)
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

    show_image(Imagen_con_SVD,nm)

def show_image(i,n):
    cv2.imshow(n,i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main():
    parser = argparse.ArgumentParser(prog="SVD2",description="Programa para reducir la dimensiomalidad de una imagen.")
    parser.add_argument('-src', '--source', type=check_file, required=True, help='Imagen fuente')
    parser.add_argument('-dest', '--destination', type=check_extension, default="output_image.png", help='Imagen reducida')
    parser.add_argument('-sigb', '--signif_bytes',type=int, required=True, help='Número de bytes significativos para apliación de reducción')

    args = parser.parse_args()
    redux(args)

if __name__ == "__main__":
    main()
