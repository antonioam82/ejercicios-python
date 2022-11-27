from cryptography.fernet import Fernet

def genera_clave():
	clave = Fernet.generate_key()
	with open("clave.key","wb") as archivo_clave:
		archivo_clave.write(clave)

def cargar_clave():
	return open("clave.key","rb").read()

genera_clave()
clave = cargar_clave()
mensaje = "Mi mensaje".encode()

f = Fernet(clave)
encriptado = f.encrypt(mensaje)
print(encriptado)

dessen = f.decrypt(encriptado)
print(dessen)
