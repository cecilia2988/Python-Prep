# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>


class Vehiculo:
    color = str
    cilindrada = int
    tipo = str
    velocidad = float
    direccion = str


    def __init__(self,color,cilindrada,tipo, velocidad,dir):
        self.color = color
        self.cilindrada= cilindrada
        self.tipo= tipo
        self.velocidad = velocidad 
        self.direccion = dir  


    def Acelerar(self, vel):
        self.velocidad+=vel

    def Frenar(self, vel):
        self.velocidad -=vel

    def Doblar(self, dir):
        self.direccion=dir