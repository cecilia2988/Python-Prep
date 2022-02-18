#2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en 
# grados centígrados, un valor de humedad y por último si llovio (Con True o False). 
# Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una 
# marca de tiempo y esa información.

import datetime
import sys

if len(sys.argv)==4:
    temperatura=sys.argv[1]
    humedad=sys.argv[2]
    llovio=sys.argv[3]
    hoy =datetime.datetime.now()
    marcadetiempo= int(datetime.datetime.timestamp(hoy))
    linea = str(marcadetiempo) + "," + temperatura + "," + humedad + "," + llovio

    with open("./datostemperatura.csv","w") as f:
        f.write(linea)
        f.write("\n")
        
else:
    print("Por favor ingrese correctamente los parametros temperatura humedad llovio ejemplo 30 40 True")

