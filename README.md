# DEEPL
## Datentypen
### bool
Wert für wahr oder falsch</br>
leere Kollektionen und Zahlen mit dem Wert null sind False</br>
Nichtleere Kollektion und alle Zahlen ungleich null sind True
### Zahl
#### int
Ganze Zahl, bei Dezimalzahlen keine führende Null erlaubt
#### float
Gleitkommazahl, als Dezimalbruch oder Exponentialschreibweise</br>
gültige Schreibweise ist: 1.30, .45, 0.45, 2.0</br>
1.0e-3 => 1x10^(-3) = 0.001</br>
2.1E+2 => 2.1x10^2 = 210
### Kollektion
#### set
Ungeordnete Kollektion ohne Duplikate, erzeugt mit geschweiften Klammern</br>
loesungsMenge = {5, 7, 10}
#### dict
besteht auf Schlüssel und Wert getrennt durch ein Doppelpunkt und in geschweiften Klammern</br>
monate = {1:"Januar", 2:"Februar"}
#### Seqzuenz
###### str
String gekennzeichnet durch Anführungszeichen sowohl "" als auch '' sind erlaubt.</br>
"Hallo 'Welt'"</br>
'Hallo "Welt"'</br>
nicht änderbar => es können keine Zeichen entfernt, hinzugefügt oder geändert werden
###### tuple
Zusammenfassung gleicher oder verschiedener Typen. Literal beginnt und endet mit runden Klammern</br>
person = ('Hans', 1999)</br>
beispiel = (1,)</br>
Tupel sind nicht änderbar
###### list
Listen sind änderbäre Sequenzen von Objekten beliebiger Art. Literal beginnt und endet mit eckigen Klammern</br>
zahlen = [1, 2, 3, 5, 6]</br>
print(zahlen[0]) -> 1</br>
zahlen[0] = 100</br>
print(zahlen[0]) -> 100


# Gemeinssame Operationen
## Kollektion
in => Überprüfen ob Element vorhanden</br>
"I" in "Team"</br>
1 in {1, 2, 3}

len() => Größe einer Kollektion</br>
len("Name") -> 4</br>
len([1,2]) -> 2

Iteration sind auf alle Arten von Kollektion möglich


