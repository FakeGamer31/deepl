from volumen import *

summe = 0  # 2
eingabe = input('(Q)uader, (K)uppel, (E)nde: ')  # 3
while eingabe in 'kKqQ':  # 4
    if eingabe in 'kK':  # 5
        h = float(input('Höhe (m): '))
        r = float(input('Radius (m): '))
        n = int(input('Anzahl dieser Kuppeln: '))
        summe += n * kuppel(h, r)  # 6
    elif eingabe in 'qQ':
        l = float(input('Länge (m): '))
        b = float(input('Breite (m): '))
        h = float(input('Höhe (m): '))
        n = int(input('Anzahl dieser Quader: '))
        summe += n * quader(l, b, h)
    eingabe = input('(Q)uader, (K)uppel, (E)nde: ')  # 7
print('Das Volumen des Gebäudes ist ',
      round(summe, 2), 'm²')
