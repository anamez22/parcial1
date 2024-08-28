class Accesorio:

    def __init__(self,color,marca):

        self.color=color
        self.marca=marca

pandora=Accesorio("plateado", "pandora")


print(type(pandora))


print(pandora.color, pandora.marca)
