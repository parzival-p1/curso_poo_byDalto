
###***  D  E  C  O  R  A  D  O  R  E  S ***###

'''
Los decoradores son funciones que decora a otras
funciones

- El decorador toma la func y le agrega funcionalidad 
antes y/o después de ejecutarla
'''

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la función")
    return funcion_modificada

#* Esto hace la fun decorador
# def saludo():
#     print("Hola Dalto como andas")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    ''' func saludar '''
    print("Hola Paco como andas")

saludo()
