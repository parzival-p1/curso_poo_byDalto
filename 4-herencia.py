
###*** H E R E N C I A  S I M P L E  P O O ***###

'''
La herencia permite a la clase hija (sublclase)
acceder a todos los metodos y tener las props de
la clase padre (superclase)
'''

class Persona:
    ''' Clase Padre Persona '''

    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        ''' metodo hablar '''

        print(f"Hola mundo! soy {self.nombre}")

class Empleado(Persona): #* De esta manera Empleado hereda los att de persona
    '''Clase hija empleado'''

    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):

        #* la func super() hereda los attributos de la clase padre Persona
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    #* También es posible sobreescribir los metodos
    def hablar(self):
        print("No habalar")

class Estudiante(Persona):
    ''' Segunda clase estudiante'''

    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

roberto = Empleado("Roberto", 25, "peruano", "Programador", 1000000)
print(roberto.edad)
roberto.hablar()
