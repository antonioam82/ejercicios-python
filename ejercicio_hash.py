import hashlib
from PIL import Image

#CALCULA VALOR HASH DE LOS ARCHIVOS USANDO EL ALGORITMO 'SHA256'
def calcular_hash(nombre_archivo, algoritmo='sha256'):
    hash_obj = hashlib.new(algoritmo)
    with open(nombre_archivo, 'rb') as archivo:
        while True:
            bloque = archivo.read(65536)  # Leer en bloques de 64 KB
            if not bloque:
                break
            hash_obj.update(bloque)
    return hash_obj.hexdigest()

#COMPARA 2 ARCHIVOS DE IMAGEN USANDO SUS HASHES
def comparar_imagenes(imagen1, imagen2):
    hash1 = calcular_hash(imagen1)
    hash2 = calcular_hash(imagen2)
    print(f"El hash de '{imagen1}' es {hash1}.")
    print(f"El hash de '{imagen2}' es {hash2}.")
    
    if hash1 == hash2:
        return True
    else:
        return False

# COMPARACION DE IMAGENES
imagen1 = 'portrait.jpg'
imagen2 = 'portrait_copia.jpg'

if comparar_imagenes(imagen1, imagen2):
    print(f"\nLas imágenes '{imagen1}' y '{imagen2}' son idénticas.")
else:
    print(f"\nLas imágenes '{imagen1}' y '{imagen2}' son diferentes.")
