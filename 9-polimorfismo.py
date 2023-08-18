
###*** P  O  L  I  M  O  R  F  I  S  M  O ***###

'''
Poli-morfismo: Multiples formas

- Todas las variables en Python 🐍 son polimorfas ya
que pueden tomar distintos tipos de datos, esto es:
polimorfismo en tiempo de ejecucion o polimorfimso
de inclusion
'''
class Animal(): #* Tipo real: origen 
    def sonido(self):
        pass

class Gato(Animal):
    ''' Clase felino '''
    def sonido(self):
        return 'Miaww'

class Perro(Animal):
    ''' Clase can '''
    def sonido(self):
        return 'guafguaf'

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato() #* Tipo declarado: origen de var
perro = Perro()

''' El mismo metodo funciona diferente para distintos args '''
hacer_sonido(perro) # misma funnc, cambia el arg, clase u obj
hacer_sonido(gato)

''' El mismo metodo funciona distinto para diferentes objs '''
print(perro.sonido()) # mismo metodo, cambia el obj dnd se implementa
print(gato.sonido())

#*** P O L I M O R F I S M O  D E  C O H E R S I O N ***
''' e j e m p l o  1
al sumar un int + float encontramoas polimorfismo
adaptandose a distintos tipos de datos.
'''

num1 = 3.4
num2 = 4

resultado = num1 + num2
print(resultado) # 7.4
print(type(resultado)) # <class 'float'>

''' e j e m p l o  3
La siguiente funcion recorrer el elemento sin importar
el tipo de dato con int o str, una misma funcion que
recibe distintos tipos de datos sin alterar su funcionalidad
'''
def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")

lista1 = [1,2,3,4,5]
lista2 = ["maquina", "como", "andas"]

recorrer(lista1)
recorrer(lista2)

#* Tipo real: origen de todo (Padre?)
#* Tipo declarado:  origen de la variable
