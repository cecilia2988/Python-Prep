# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor


class Vehiculo:
    color = str
    cilindrada = int
    tipo = str

def __init__(self,color,cilindrada,tipo):
    self.color =color
    self.cilindrada=cilindrada
    self.tipo=tipo   