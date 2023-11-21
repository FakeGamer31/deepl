import random
import math


def wuerfel(anzahl_seiten):
    # Gebe über den Zufall eine Würfelseite zurück und gebe das
    # Ergebnis zurück
    return random.randint(1, anzahl_seiten)


# Drivers Code:
seiten = 6
ergebnis = wuerfel(seiten)
print(f'Du hast eine {ergebnis} mit einem {seiten}-seitigem Würfel gerollt')
