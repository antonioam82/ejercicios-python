import socket
import tqdm
import time

HOST = "localhost" #IP DEL SERVIDOR
PORT = 9999        #PUERTO DE ESCUCHA

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))     # ASOCIAR SOCKET A DIRECCIÓN IP Y PUERTO
server.listen()               # PONER SERVIDOR A LA ESCUCHA 

client, addr = server.accept() # ACEPTAR CONEXIONES ENTRANTES

file_name = client.recv(1024).decode()
print(file_name)                      # IMPRIME NOMBRE DEL NUEVO ARCHIVO
file_size = client.recv(1024).decode()
print(file_size)                      # IMPRIME TAMAÑO ARCHIVO

file = open(file_name, "wb")  # ABRE ARCHIVO EN MODO ESCRITURA

file_bytes = b""

size = int(file_size) # TAMAÑO DEL ARCHIVO RECIVIDO

done = False

# CREAR BARRA DE PROGRESO
progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,
                total=size) 

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data
    time.sleep(0.003)
    progress.update(1024) # ACTUALIZAR BARRA DE PROGRESO

file.write(file_bytes) # ESCRIBIR ARCHIVO

file.close()    # CERRAR ARCHIVO
client.close()  # CERRAR CLIENTE
server.close()  # CERRAR SERVIDOR

