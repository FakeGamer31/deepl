import math as m


def baumhoehe(entfernung, augenhoehe, winkel):
    return round(augenhoehe + (m.tan(m.radians(winkel)) * entfernung), 2)


entfernung = float(input('Entfernung zum Baum (m): '))
augenhoehe = float(input('Augenhöhe (m): '))
winkel = float(input('Blickwinkel (Grad): '))

print(baumhoehe(entfernung, augenhoehe, winkel))
