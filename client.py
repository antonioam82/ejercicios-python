import socket

#CONECTA, ENVIA Y RECIBE INFORMACIÓN DEVUELTA DESE "server.py"

HOST = "127.0.0.1" #
PORT = 65123 #Puerto de envio

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Hola mundo")

    data = s.recv(1024)

print("Recibido", repr(data))
