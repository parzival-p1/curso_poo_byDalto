
###*** H E R E N C I A  P O O ***###

'''
La herencia permite a la clase hija (sublclase)
acceder a todos los metodos y tener las props de
la clase padre (superclase)

- super() la usamos para llamar a una Clase Padre
'''

class Persona:
    '''Clase Persona'''

    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        ''' metodo hablar '''
        print("Hola, estoy paralando!")


class Artista:
    ''' Clase Artista con habilidades '''

    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        ''' metodo mostrar su habilidad '''
        return f"Mi habiilidad es: {self.habilidad}"

#*** *** herencia multiple *** ***#
class EmpleadoArtista(Persona, Artista):
    ''' Clase de herencia multiple '''

    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario

    #* usando super() para especificar la herencia
    def presentarse(self):
        ''' metodo presentarse '''

        print(f'Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

#* en este caso super() indica que es un metodo heredado 

class Estudiante(Persona):
    ''' subclase Estudiante super clase Persona '''
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):

        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad


roberto = EmpleadoArtista("Roberto", 25, "peruano", "Cantar", "LinkedIn", 1000000)
print(roberto.edad)
roberto.presentarse()

#*** Cómo saber si es una subclase?
herencia_1 = issubclass(EmpleadoArtista, Artista)
herencia_2 = issubclass(Artista, Persona)

print(herencia_1) # if True = subclass
print(herencia_2) # if False = different classes

#*** Cómo saber si es una instancia?
instancia = isinstance(roberto, Artista)
print(instancia) # True, roberto es unn obj de la clase Artista
