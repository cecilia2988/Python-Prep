'''
1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera
 arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero 
 ¿qué pasa si se envía otro tipo de dato?
 '''
# import sys
# sys.path.append(r'C:\Users\rmcec\OneDrive\Documentos\Data\Python-Prep\07 - Classes & OOP\ejercicio8.py')

import misherramientas as h

def run():
    objeto = h.Herramientas([1,2,"hola"])
    objeto.verifica_primo()

    #Typeerror




if __name__=='__main__':
    run()