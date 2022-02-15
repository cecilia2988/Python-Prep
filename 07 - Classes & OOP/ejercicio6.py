# 6) Probar las funciones incorporadas en la clase del punto 5

from ejercicio5 import MisFunciones

def run():
    mf =MisFunciones()
    print(mf.calcularconversion("Celcius",100,"Kelvin"))
    print(str(mf.Esprimo(11)))
    print(mf.fac(5))



if __name__=='__main__':
    run()