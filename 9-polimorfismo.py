
###*** P  O  L  I  M  O  R  F  I  S  M  O ***###

'''
Poli-morfismo: Multiples formas

- Todas las variables en Python 🐍 son polimorfas ya
que pueden tomar distintos tipos de datos, esto es:
polimorfismo en tiempo de ejecucion o polimorfimso
de inclusion
'''

class Gato():
    ''' Clase felino '''
    def sonido(self):
        return 'Miaww'

class Perro():
    ''' Clase can '''
    def sonido(self):
        return 'guafguaf'

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

''' El mismo metodo funciona diferente para distintos args '''
hacer_sonido(perro) # misma funnc, cambia el arg, clase u obj
hacer_sonido(gato)

''' EL mismo metodo funciona distinto para diferentes objs '''
print(perro.sonido()) # mismo metodo, cambia el obj dnd se implementa
print(gato.sonido())

