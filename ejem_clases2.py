
# DECLARAMOS CLASE "CuentaBancaria"
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente.")

    def obtener_saldo(self):
        return self.__saldo

# CREAMOS OBJETO DE LA CLASE "CuentaBancaria"
cuenta = CuentaBancaria("Juan", 1000)

# ACCEDEMOS AL ATRIBUTO PRIVADO "saldo" A TRAVÉS DE MÉTODO PÚBLICO
print(cuenta.obtener_saldo())

# SI IENTENTAMOS ACCEDER DIRECTAMENTE AL ATRIBUTO PRIVADO SE GEBERARÁ
# UN ERROR
print(cuenta.__saldo)
