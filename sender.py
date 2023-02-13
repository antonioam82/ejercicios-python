import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",9999))

file = open("image.png", "rb")
file_size = os.path.getsize("image.png")

client.send("received_image.png".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()
