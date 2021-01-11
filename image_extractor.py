import fitz # PyMuPDF
import io
import os
from PIL import Image

#ESTABLECER DIRECTORIO DE TRABAJO.
#os.chdir(r'C:\Users\Antonio\Documents\Mis programas\pdf_images')

#NOMBRE ARCHIVO PDF.
file = "1710.05006.pdf"
#ABRIR PDF.
pdf_file = fitz.open(file)
#RECORRER PÁGINAS DEL PDF.
for page_index in range(len(pdf_file)):
    #LEER PÁGINA
    page = pdf_file[page_index]
    image_list = page.getImageList()
    #MOSTRAR NÚMERO DE IMÁGENES ENCONTRADAS
    if image_list:
        print(f"[+] Se encontraron {len(image_list)} imágenes en la página {page_index}")
    else:
        print("[!] No se encontraron imágenes en la página", page_index)
    for image_index, img in enumerate(page.getImageList(), start=1):
        #REFERENCIAS EXTERNAS DE LA IMAGEN.
        xref = img[0]
        #BYTES DE LA IMAGEN
        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]
        #EXTENSION DE LA IMAGEN.
        image_ext = base_image["ext"]
        #ABRIR CON PIL.
        image = Image.open(io.BytesIO(image_bytes))
        #ALMACENAR ARCHIVO DE IMÁGEN.
        image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
