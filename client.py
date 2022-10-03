import socket

HOST = "localhost"#"127.0.0.1" #IP DEL SERVIDOR
PORT = 65123 #PUERTO DE ENVIO

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))     # SOLICITUD DE CONEXIÓN CON SERVIDOR

    s.sendall(b"Hola mundo")    # ENVIAR DATOS AL SERVIDOR
    data = s.recv(1024)         # ESPERA A RECEPCIÓN DE INFORMACIÓN DEL SERVIDOR

print("Recibida", repr(data))

