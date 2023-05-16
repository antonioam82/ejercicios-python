
# CLASE "Persona"
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# CREAMOS OBJETOS DE LA CLASE "Persona"
persona1 = Persona("Juan", 25)
persona2 = Persona("Maria", 30)

# LLAMAMOS AL MÉTODO "saludar" DE AMBOS OBJETOS.
persona1.saludar()
persona2.saludar()


# DECLARAMOS CLASE
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estoy en el curso {self.curso}.")


# CREAMOS OBJETO DE LA CLASE "Estudiante"
estudiante1 = Estudiante("Pedro", 20, "Matemáticas")

# LLAMAMOS A LOS MÉTODOS HEREDADOS DE LA CALSE "Persona"
estudiante1.saludar()

# LLAMAMOS EL MÉTODO "presentarse" DE LA CLASE "Estudiante"
estudiante1.presentarse()
