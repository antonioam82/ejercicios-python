import getpass

database = {"user1": "12345", "user2": "6789"}

username = input("Introduce usuario: ")

if username in database:
    password = getpass.getpass("Contraseña: ")
    while password != database[username]:
        password = getpass.getpass("Contraseña no válida. Intenta de nuevo: ")
    print("Usuario verificado")
else:
    print("Usuario no encontrado")
