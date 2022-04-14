"""
Este archivo contiene la definción de la clase Coordenada
"""


class Coordenada:
    """
    Clase que modela una coordenada en un plano cartesiano x_coord, y coord
    """
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def distancia(self, otra_coordendada):
        """ Calcula la distancia entre dos coordenadas """
        x_coord_diff = (self.x_coord - otra_coordendada.x_coord)**2
        y_coord_diff = (self.y_coord - otra_coordendada.y_coord)**2

        return (x_coord_diff + y_coord_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(3, Coordenada))
