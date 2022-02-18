import animal

class Perro(animal.Animal):
    def __init__(self,nombre,edad,raza,color) -> None:
        animal.Animal.__init__(self,nombre,edad)
        self.raza=raza
        self.color=color

    def DefinirRaza(self):
        print("Mi raza es ", self.raza)