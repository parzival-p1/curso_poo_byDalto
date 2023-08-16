
###*** E J E R C I C I O S  P O O  H E R E N C I A ***###

'''  H e r e n c i a  m ú l t i p l e  y  M R O

Imagina que estás modelando animales en un Zoo.
Crea tres clases: "Animal", "Mamifero" y "Ave".

- La clase "Animal" debe tener un método llamado
"comer".
- La clase "Mamifero" debe tener un método llamado
"amamantar"
- La clase "Ave" debe tener un método llamado
"volar"

- Ahora, crea una clase "Murciélago" que herede de
"Mamifero" y "Ave", en ese orden, y por lo tanto
sea capaz de "amamantar" y "volar", admás de "comer"

–*  Finalmente, nuega con el orden de herencia de la
cclase "Murciélago" y observa cómo cambai el MRO
y el comportamient de los métodos al usar super()
'''

class Animal:
    ''' super Clase Animal '''

    def comer(self):
        ''' método comer '''
        print("El animal esta comiendo")

class Mamifero(Animal):
    ''' subclase Mamifero '''

    def amamantar(self):
        ''' metodo amamantar  '''
        print("El mamifero esta amamantado")

class Ave(Animal):
    ''' subclase Ave '''

    def volar(self):
        ''' método volar '''
        print("El ave esta volando")

class Bat(Mamifero, Ave):
    ''' clase de herencia multiple '''
    pass

murcielago = Bat()
murcielago.comer() # El animal esta comiendo
murcielago.amamantar() # l mamifero esta amamantado
murcielago.volar() # El ave esta volando

#*** M R O
print(Bat.mro())
