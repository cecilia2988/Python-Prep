# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
from ejercicio4 import Vehiculo



def run():
   
    mivehiculo= Vehiculo("Azul", 100, "Auto", 5, "asdsa")
    mivehiculo.Acelerar(100)
    mivehiculo2=Vehiculo("Negro",200,"Moto",200,"Sur")
    mivehiculo2.Frenar(5)
    mivehiculo3=Vehiculo("Amarillo",100,"Camion",45,"Norte")
    mivehiculo3.Doblar("Oeste")
    print(vars(mivehiculo))
    print(vars(mivehiculo2))
    print(vars(mivehiculo3))
    mivehiculo.Estado()
 

if __name__=='__main__':
    run()

