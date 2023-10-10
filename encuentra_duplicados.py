import os
import hashlib

def calcular_hash_sha256(nombre_archivo):
    """Calcula el hash SHA-256 de un archivo."""
    sha256 = hashlib.sha256()
    with open(nombre_archivo, "rb") as archivo:
        while True:
            bloque = archivo.read(65536)  # Lee en bloques de 64 KB
            if not bloque:
                break
            sha256.update(bloque)
    return sha256.hexdigest()

def encontrar_duplicados(directorio):
    """Encuentra archivos duplicados en un directorio basándose en sus hash SHA-256."""
    hash_dict = {}
    duplicados = []

    # Itera sobre todos los archivos en el directorio
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            hash = calcular_hash_sha256(ruta_completa)

            # Si el hash ya existe en el diccionario, se encuentra un duplicado
            if hash in hash_dict:
                duplicados.append((hash, ruta_completa))
            else:
                hash_dict[hash] = ruta_completa

    return duplicados

if __name__ == "__main__":
    directorio_busqueda = "/ruta/a/tu/directorio"  # Reemplaza esto con la ruta de tu directorio
    resultados = encontrar_duplicados(directorio_busqueda)

    if resultados:
        print("Archivos duplicados encontrados:")
        for hash, ruta in resultados:
            print(f"Hash: {hash}\nRuta: {ruta}\n")
    else:
        print("No se encontraron archivos duplicados en el directorio.")
