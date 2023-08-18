
###*** M E T H O D  R E S O L U T I O N  O R D E R ***#

''' M  R  O
Hace referencia al orden en el que Python 🐍
busca metodos y atributos en las clases
'''
class A:
    ''' Clase A '''

    def hablar(self):
        ''' hablar func '''
        print("Hola desde: A") 

class F(A):
    ''' Clase F '''

    def hablar(self):
        print("Hola desde: F")

class B(A):
    ''' clase B '''

    def hablar(self):
        ''' hablar func '''
    print("Hola desde: B")

class C(A):
    ''' Clase C '''

    def hablar(self):
        ''' hablar func '''
        print("Hola desde: C")

class D(B, C):
    ''' Clase D '''
    def hablar(self):
        print("Hola desde D")

d = D() # objeto
d.hablar() # clase que deseo llamar
print(D.mro)

#*** Función de orden MRO
