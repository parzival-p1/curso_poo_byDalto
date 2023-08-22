
##*** G e t t e r s  y  S e t t e r s ***##

'''
Metodos para acceder a propiedades privadas que tienen
las clases y modificar los valores de una clase
'''

class Persona:
    ''' clase Persona '''
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        ''' getter: func que accede al valor
        del atributo'''
        return self.__nombre

    def set_nombre(self, new_nombre):
        ''' setter: func que define el valor
        del atributo '''
        self.__nombre = new_nombre

dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Chepo")

nombre = dalto.get_nombre() # trae el nuevo nombre 'Chepo'
print(nombre)
