"""
Frage 1: Wahr oder nicht wahr?
Tragen Sie in die Tabelle die Wahrheitswerte der Ausdrücke ein.
Ausdruck                                Wahrheitswert
'a' not in 'Sonne'                      True
(1 == 1) and (1 == 2)                   False
not(2 > 2)                              True
type(1) == type(2)                      True
str(1) in str(123)                      True
bool('sein') or not bool('sein')        True
(True or False) and (True and False)    False
2 < 3 < 1                               False
"""
print('a' not in 'Sonne')
print((1 == 1) and (1 == 2))
print(not(2 > 2))
print(type(1) == type(2))
print(str(1) in str(123))
print(bool('sein') or not bool('sein'))
print((True or False) and (True and False))
print(2 < 3 < 1)

"""
Frage 2: Bedingung
Bei einer Variante des Wissenstests brauchen nur sechs der acht Planeten aufgezählt zu werden. Wie lautet die passende Bedingung für die while-Anweisung?

while len(planeten) > 2:
"""

# planeten = {'Merkur', 'Venus', 'Erde', 'Mars',
#             'Jupiter', 'Saturn', 'Uranus', 'Neptun'} #1
# print('Zähle alle Planeten unseres Sonnensystems auf!')
# #while planeten != set(): #2
# while len(planeten) > 2:
#     eingabe = input('Planet: ')
#     if eingabe in planeten:
#         planeten = planeten - {eingabe} #3
#         print('Richtig!')
#     else:
#         print('Sorry!', eingabe, 'hatten wir schon oder',
#       eingabe, 'ist kein Planet') #4
# print('Glückwunsch. Du hast alle Planeten aufgezählt.') #5

#Übung 1 Grundumsatz
mass = float(input("Wie viel wiegen Sie? (Gewicht in kg): "))
height = float(input("Wie gross sind Sie? (Groesse in cm): "))
age = float(input("Wie alt sind Sie? (Alter in Jahre): "))
sex = input("Sind sie ein Mann oder eine Frau? (m/f): ")
grundumsatz = 0.0
if sex == "m":
    grundumsatz = 66.5 + 13 * mass + 5 * height - 6.8 * 5
elif sex == "f":
    grundumsatz = 665 + 9.6 * mass + 1.8 * height - 4.7 * 5
print("Ihr Grundumsatz betraegt", grundumsatz)