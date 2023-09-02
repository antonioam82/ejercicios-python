import cv2
import numpy as np
from scipy.linalg import svd
import argparse
from colorama import init, Fore, Style


def main():
    parser = argparse.ArgumentParser(prog="SVD2",description="Programa para reducir la dimensiomalidad de una imagen.")
    parser.add_argument('-src', '--source', required=True, help='Imagen fuente')
    parser.add_argument('-dest', '--destination', default="output_image.mp4", help='Imagen reducida')
    parser.add_argument('-sigb', '--signif_bytes', required=True, help='Número de bytes significativos para apliación de reducción')

    args = parser.parse_args()


if __name__ == "__main__":
    main()
