
### *** P  R  O  P  I  E  D  A  D  E  S *** ###

#*** *** @property *** ***#
'''
Las propiedades son getters y setters (y deleters
para eliminar valores, metodos etc)
'''

class Persona:
    ''' Clase Persona '''
    def __init__(self, nombre, edad):
        self.__nombre = nombre #^ nombre real de la variable
        self._edad = edad

    @property #^ esto es un getter oculta el nombre real de la variable
    def nombre(self):
        ''' func get_nombre '''
        return self.__nombre

    @nombre.setter  #^ esto es un setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter #^esto es un deleter
    def nombre(self):
        del self.__nombre 

paco = Persona("Lucas", 21)

nombre = paco.nombre
print(nombre)

#* Setter que modifica el valor del  nombre Lucas
paco.nombre = "Pepe"

# paco.nombre = "Pepes" #! AttributeError: can't set attribute

#* Propiedad modificada
nombre = paco.nombre
print(nombre)

#* Usando un @deleter
del paco.nombre

# nombre = paco.nombre #! AttributeError: 'Persona' object has no attribute '_Persona__nombre'
print("La propieda nombre se ha borrado correctamente")
