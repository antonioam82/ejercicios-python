import socket

HOST = "127.0.0.1" # ESTABLECEMOS DIRECCIÓN
PORT = 65123       # PUERTO DE ESCUCHA

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))       # ASOCIAR SOCKET A DIRECCIÓN IP Y PUERTO
    s.listen()                 # PONER SOCKET A LA ESCUCHA
    conn, addr = s.accept()    # ESPERAR CONEXIONES ENTRANTES

    with conn:
        print(f"Conexión establecida con {addr}:")
        while True:
            data = conn.recv(1024)  # RECIBE DATOS DEL CLIENTE
            if not data:
                break

            conn.sendall(data)      # DEVUELVE LOS DATOS AL CLIENTE


            
