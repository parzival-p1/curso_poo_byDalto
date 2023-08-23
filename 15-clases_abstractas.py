from abc import ABC, abstractmethod # abstractmethod es un decorador que indica a la clase que es un metodo abstracto

### *** C L A S E S  A B S T R A C T A S *** ###

class Persona(ABC):
    ''' esto es una clase abstracta, uma plantisha
    que nos permite crear personas '''
    @abstractmethod
    def __init__ (self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola! me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    ''' Estudiante es una subclase de Persona '''
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    ''' Trabajador es una subclase de Persona '''
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en el rubro de: {self.actividad}")

class Entrepreneur(Estudiante, Trabajador):
    ''' clase Entrpreneur es una subclase de Persona '''
    def __init__(self, nombre, edad, sexo, actividad, emprender):
        super().__init__(nombre, edad, sexo, actividad)
        self.emprender = emprender

    def hacer_actividad(self):
        print(f"Estoy trabajando en el Rubro de la {self.hacer_actividad}")

    def emprendiendo(self):
        print(f"Estoy emprendiendo en el rubro de {self.emprender}")


paco = Estudiante("Paco", 21, "Masculino", "programacion")
dalto = Trabajador("Dalto", 25, "Masculiino", "programacion")
paco = Entrepreneur("Paco", 30, "masculino", "progrmacion", "tecnologia")

#* Clase Estudiante
paco.presentarse()
paco.hacer_actividad()

#* Clase Trabajador
dalto.presentarse()
dalto.hacer_actividad()

#* Clase Entrepreneur
paco.presentarse()
paco.emprendiendo()

