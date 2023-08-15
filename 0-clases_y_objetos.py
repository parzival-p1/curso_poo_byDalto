
###*** C L A S E S  Y  O B J E T O S ***###

#* MARCA
cel1_marca = "samsung"
cel2_marca = "apple"
cel3_marca = "huawei"

#* MODELO
cel1_modelo = "s23"
cel2_modelo = "iPhone 14"
cel3_modelo = "P20 Pro"

#* CAMARA FRONTAL
cel1_camaraT = "48MP"
cel2_camaraT = "48MP"
cel3_camaraT = "12MP"

#* CAMARA TRASERA
cel1_camaraF = "24MP"
cel2_camaraF = "24MP"
cel3_camaraF = "8MP"

print(cel2_camaraT)


#*** DEFINNICION DE CLASES y OBJETOS ***#
class Celular():
    '''Clase celular'''

    marca = "Samsung"  # static attributes
    modelo = "S23"    # static attributes
    camara = "48MP"  # static attributes

celu1 = Celular() # obj es una instancia de la clase
celu2 = Celular() # instanciar un obj = crear un obj
celu3 = Celular() # obj es una prop del obj principal que es __main__
celu4 = Celular() # celu4 es una instancia de la clase Celular()
'''Todos los obj que creamos son instancias de otras clases'''

# cambiando valores
celu3.camara = "49mp"
print(celu3)
