import numpy as np


def paarweise_Summe(values, weight):
    # Berechne die Paarweise Summe. Die Verwendung von np.sum st nicht gestattet
    # Und gebe das korretke Ergebnis zurück
    if len(values) != len(weight):
        raise ValueError('Die Längen der Arrays müssen gleich sein.')

    result = 0
    for values, weights in zip(values, weight):
        result += values * weights

    return result


# Drivers Code:
values = np.array([1, 2, 3, 4, 5])
weights = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

result = paarweise_Summe(values, weights)
print('Ergebnis der paarweisen Summe: ', result)
