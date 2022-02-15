# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se
#  encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

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


    def Estado(self):
        print("Velocidad ",self.velocidad, "Direccion ",self.direccion)  

    def Caracteristicas(self):
        print("Color ", self.color, "Tipo ", self.tipo, "cilidrada ", self.cilindrada)      