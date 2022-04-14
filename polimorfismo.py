
class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print("Estoy avanazando!")


class Peaton(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        super().avanza()
        print("Uso mis pies para avanzar")


class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        super().avanza()
        print("Ando moviendome en bicicleta")


if __name__ == "__main__":
    bren = Peaton("Brendita")
    karlos = Ciclista("Karlos")

    bren.avanza()
    karlos.avanza()
