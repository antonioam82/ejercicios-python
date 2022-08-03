import pickle

class Vehiculo:
    marca = ""
    num_ruedas = 0.0

    def __init__(self, marca, num_ruedas):
        self.marca = marca
        self.num_ruedas = num_ruedas

    def getMarca(self):
        return self.marca


v1 = Vehiculo("seat", 4)

f = open('datos.bin','wb')
pickle.dump(v1, f)#SERIALIZACION
f.close()

f = open('datos.bin', 'rb')
vehiculo = pickle.load(f)#DESERIALIZACIÓN
f.close()

print(vehiculo.getMarca(), "número de ruedas: ", vehiculo.num_ruedas)
