
### *** A  B  S  T  R  A  C  C  I  O  N *** ###

''' C O N C E P T O
Manejar la complejidad de la logica ocultando todos
los detalles inecesarios al programador o al usuario.

Interfaz simple que oculte la interfaz compleja

- Ej, no es necesario entender como funciona la
mecanica innterna de un auto para poder conducirlo
'''
class Auto():
    ''' clase Auto '''
    def __init__(self):
        self.__estado = "apagado"

    def encender(self):
        self.__estado = "encendido"
        print("El auto esta encendido")
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()
