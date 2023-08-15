
###*** A T R I B U T O S  Y  C O N S T R U C T O R ***###

'''Los atributos son variables que pertenecen a una clase'''

#* F A B R I C A  D E  C E L U L A R E S *#
class Celular:
    '''Celular y atributos Y
    El Metodo Constructor '''

    def __init__(self, marca, modelo, camara):
# crea la prop self  # accede a un param
        self.marca  = marca  # "Samsung"
        self.modelo = modelo  # "S23"
        self.camara = camara   # "48MP"

celu1 = Celular("Samsung", "S23", "48MP")
celu2 = Celular("Apple", "Iphone 15 ProMax", "96MP")

print(celu1.marca)
print(celu2.marca)
