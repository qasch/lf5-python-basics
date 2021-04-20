# Dokumentation Python Basics - LF5

## Entwicklungstools

Nach dem Download von `python` stehen folgende Tools zur Verfügung:

* Python Shell: 
  * zum Ausführen von *Codeschnippseln/Snipppets*
  * für Tests (ob z.B. etwas vom prinzip her so funktioniert wie man denkt)
  * kann als Taschenrechner genutzt werden
  * usw.

* Python IDE *IDLE*: 
  * "vollständige" Entwicklungsumgebung
  * hier wird der Quelltext geschrieben
  * *Quick Tipps* für Parameter
  * Debugger enthalten 
  * mehrere Dateien ergeben zusammen ein grösseres Programm

* SQLite Datenbank:
  * komplettes, *ausgewachsenes* Datenbankmanagement System (DBMS)
  
  
## Variablen

* Variablen können Werte aufnehmen
* auf diese Werte kann über den Namen der Variable wieder zugegriffen werden
* der Name kann beliebig gewählt werden
  * bestimmte Zeichen sind aber nicht erlaubt (z.B. Sonderzeichen ausser dem `_`, Zahlen als erstes Zeichen)
  * Variablen sollten eindeutig und sprechend benannt werden
* nützlich, um mehrmals auf den gleichen Wert/Inhalt zugreifen zu können
* können ihren Inhalt im Laufe des Programms ändern (*Variable/variabel*)

# Datentypen

## Integer
* Ganze (natürliche) Zahl
* in Python: `int`
* z.B. `5`

## Float
* Fliesskommazahl
* engl. "to float" <=> "fliessen"
* in Python: `float`
* z.B. `5.23452`

## String
* Text
* muss entweder in einfache oder doppelte Hochkommata eingefasst werden
* in Python: `str`
* z.B. `"Hallo"`

## Boolean
* Wahrheitswert
* entweder `True` oder `False`
* in Python: `bool`


## Casting
Umwandeln eines Datenyps in einen anderen:

- `int(4.3)`
- `float(2)`
