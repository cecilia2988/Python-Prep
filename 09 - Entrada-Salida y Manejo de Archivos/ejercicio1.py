#1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, 
# verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos


from ast import arg
import sys

if len(sys.argv)==4:
    print("Argumento 1 ", sys.argv[1])
    print ("Argumento 2 ", sys.argv[2])
    print("Argumento 3 ",sys.argv[3])
else:
    print("Cantidad de argumentos incorrecta")

