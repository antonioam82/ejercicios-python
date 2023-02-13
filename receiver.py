import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")

file_bytes = b""

done = False

progress = tqdm(unit="B", unit_scale=True, unit_divisor=1000,
                total=int(file_size))

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data
    progress.update(1024)

file.write(file_bytes)

file.close()
client.close()
server.close()
