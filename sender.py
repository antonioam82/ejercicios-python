import os
import socket

HOST = "localhost" #IP DEL SERVIDOR
PORT = 9999        #PUERTO DE ENVIO

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT)) # SOLICITUD DE CONEXION CON SERVIDOR

file = open("image.png", "rb")  # ABRIR ARCHIVO A TRANSFERIR
file_size = os.path.getsize("image.png") # OBTENER TAMAÑO ARCHIVO

client.send("copied_image.png".encode()) # ENVIAR NOMBRE DE NUEVO ARCHIVO
client.send(str(file_size).encode())       # ENVIAR TAMAÑO ARCHIVO

data = file.read()    # LEER INFORMACIÓN DEL ARCHIVO
client.sendall(data)  # ENVIAR INFORMACIÓN DE ARCHIVO AL SERVIDOR
client.send(b"<END>") # MARCADOR DE FIN DE DATOS

file.close()   # CERRAR ARCHIVO
client.close() # CERRAR CLIENTE
