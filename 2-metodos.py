
###*** M  E  T  O  D  O  S ***###

'''
Los metodos son funcion() que puede realizar el
objeto.
– Todas las funciones creadas dentro de una clase se llaman metodos

Ejemplo: el perro puede ladrar, correr, comer etc
'''
class Celular():

    '''Metodo constructor de celulares'''
    def __init__(self, marca, modelo, camara):
        self.marca  = marca
        self.modelo = modelo
        self.camara = camara

    '''
        Metodos definidor de funciones del Celular()
    '''

    def llamar(self):
        '''Funcion llamar'''
        print(f"Estas llamando desde tu {self.modelo} 📲")

    def colgar(self):
        '''Funcion colgar'''
        print(f"La llamada ha finalizado en tu {self.modelo}")

celu1 = Celular("Samsung", "S23", "48MP")
celu2 = Celular("Apple", "Iphone 15 ProMax", "96MP")

print(celu1.camara)

celu1.llamar()
celu1.colgar() # La llamada ha finalizado
