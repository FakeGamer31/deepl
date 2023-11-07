from math import pi


def kuppel(höhe: float, radius: float) -> float:
    'Volumen eines halben Rotationsellipsoiden'
    return 2 / 3 * pi * radius ** 2 * höhe


def quader(länge: float, breite: float, höhe: float) -> float:
    'Volumen eines Quaders'
    return länge * breite * höhe


if __name__ == '__main__':
    print('Kuppel mit Radius 1 und Höhe 1 ',
          kuppel(1, 1))
    print('Quader mit den Seitenlängen 2, 3, 2: ',
          quader(2, 3, 2))
