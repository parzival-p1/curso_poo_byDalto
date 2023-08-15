
###*** E J E R C I C I O S  P O O ***###

''' Crea una clase Estudiante con atributos:
    – Nombre, Edad, Grado '''

class Estudiante:
    '''Estudiante de prepa'''

    def __init__(self, nombre, edad, grad):
        self.nombre = nombre
        self.edad  = edad
        self.grad = grad

estudiante1 = Estudiante("Poncho", 16, 5)
print(estudiante1.nombre)
