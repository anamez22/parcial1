class Mascota:

    def __init__(self,nombre,marca):

        self.nombre=nombre
        self.marca=marca

samsung=celular("negro", "samsung")
phone=celular("azul", "phone")

print(type(samsung))
print(type(phone))

print(samsung.nombre, samsung.marca)
print(phone.nombre, phone.marca)