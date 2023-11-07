def nachricht(text: str = '', an: str = ' Mensch') -> str:
    """
    Bsp-Methode die Zeug macht
    :param text: default ''
    :param an: default ' Mensch'
    :return:
    """
    return 'Hallo ' + an + '! ' + text


print(nachricht('Tina', 'Montag geht klar.'))  # Hallo Montag geht klar.! Tina
print(nachricht(an='Tina'))  # Hallo Tina!
print(nachricht('Kopf hoch!'))  # Hallo  Mensch! Kopf hoch!


def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n - 1)


input = input('Zahl: ')
fak = fak(int(input))
print('fak von ', input, ': ', fak)

# Uebung 1 Volumen einer Platte
def volume_plate(l, b, d=2):
    return l * b * d


print(volume_plate(10, 10))
print(volume_plate(b=10, l=10, d=30))

#Uebung 2 Ziffern zählen
def count_digit(text: str):
    def rek(text, n):
        if n < 0:
            return 0
        else:
            count = text.count(str(n))
            return count + rek(text, n-1)
    return rek(text,9)


print(count_digit('12345678901012121155668877'))
print(count_digit('Python 3'))
print(count_digit('Heute ist der 11.11.2020.’'))
