
###*** E N C A P S U L A M I E N T O ***###

'''

'''
class miClase:
    def __init__(self):
        # self._atributo_privado = "valor" # atributoo priv
        self.__atributo_privado = "valor" # atributo encapsulados

    def __hablar(self):
        ''' Metodo privado '''
        print("Hola, como estás?")

objeto = miClase()
#! print(objeto.__atributo_privado) # Error att privado
#! print(objeto.__hablar()) # Acces to protected member
