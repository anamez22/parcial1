class Mascota:

    def __init__(self,nombre,especie):

        self.nombre=nombre
        self.especie=especie

coker=Mascota("copo", "perro")
bulldog=Mascota("simon", "Perro")

print(type(coker))
print(type(bulldog))

print(coker.nombre, coker.especie)
print(bulldog.nombre, bulldog.especie)