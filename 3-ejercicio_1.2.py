
###*** E J E R C I C I O S  P O O ***###

''' Crea una clase Estudiante con atributos:
    – Nombre, Edad, Grado '''

class Estudiante:
    '''Estudiante de prepa'''

    def __init__(self, nombre, edad, grad):
        self.nombre = nombre
        self.edad  = edad
        self.grad = grad

    def estudiar(self):
        '''Instancia principal del metodo estudiar'''

        print("Estudiando...")

nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
grad = input("Introduzca su grado academico: ")

estudiante1 = Estudiante(nombre,edad, grad)

print(f"""
        DATOS DEL ESTUDIANTE: \n
        Nombre: {estudiante1.nombre} \n
        Edad: {estudiante1.edad} \n
        Grado: {estudiante1.grad} 

        """)
while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante1.estudiar()
