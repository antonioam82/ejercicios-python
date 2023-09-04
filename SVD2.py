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

def main():
    parser = argparse.ArgumentParser(prog="SVD2",description="Programa para reducir la dimensiomalidad de una imagen.")
    parser.add_argument('-src', '--source', type=check_file, required=True, help='Imagen fuente')
    parser.add_argument('-dest', '--destination', type=check_extension, default="output_image.png", help='Imagen reducida')
    parser.add_argument('-sigb', '--signif_bytes',type=int, required=True, help='Número de bytes significativos para apliación de reducción')

    args = parser.parse_args()
    redux(args)

if __name__ == "__main__":
    main()
