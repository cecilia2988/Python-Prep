'''
2) En la función que hace la conversión de grados, validar que los parámetros enviados 
sean los esperados, de no serlo, informar cuáles son los valores esperados.
'''

import misherramientas as h

def run():
    objeto= h.Herramientas([2,4,5,8])
    objeto.conversion_grados("Celsius","Kelvin")




if __name__=='__main__':
    run()