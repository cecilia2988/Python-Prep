# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior.
#  Luego realizar la importación del módulo y probar alguna de sus funciones

from ejercicio7 import MisFunciones

def run():
    lista=MisFunciones([1,4,5,7,11,13,2,9,10,23])
    lista.Esprimo()
    lista.fac()



if __name__=='__main__':
    run()
