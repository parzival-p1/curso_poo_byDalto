
###*** E J E R C I C I O S  P O O  H E R E N C I A ***###

'''  - H E R E N C I A -
Herencia y uso de super

Crear un sistema para una escuela. En este sistema,
tendremos dos clases Principales: Persona y Estudiante

- La Clase Persona tendrá los atributos: nombre y edad y
un método que imprima el nombre y la edad de la
persona.

- La clase Estudiante heredará de la clase Persona y
tambén tendrá un atributo adicional: grado y un
método que imprima el grado del estudiante

-*- Deberás utilizar super en el método de inicialización
(init) para reutilizar el código de la clase padre
(Persona). Luego crea una instancia de la clase
Estudiante e imprime sus atributos y utiliza sus métodos
para asegurarte que todo funnciona correctamente.
'''

class Persona:
    ''' Super clase Persona'''

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprime_nombre(self):
        ''' método print name y edad '''
        print(f"Hola soy {self.nombre}! y tengo {self.edad} años...")

class Estudiante(Persona):
    ''' Subclase Estudiante '''

    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprime_grado(self):
        ''' método imprimir grado '''
        print(f"Mi grado es {self.grado}")

estudiante = Estudiante("David", 28, "10º")
print(estudiante.nombre)

estudiante.imprime_nombre()
estudiante.imprime_grado()
