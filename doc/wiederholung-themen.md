# Dokumentation Python Basics LF5

## Variablen

Der Name einer Variablen wird auch *Bezeichner* genannt. Bei der Vergabe eines Namens sind folgende Regeln zu beachten:
* erlaubt sind Buchstaben und Zahlen, keine Sonderzeichen
* ausser dem Unterstrich, dieser ist erlaubt (auch am Anfang eines Bezeichners oder als einzelnes Zeichen)
* obwohl Umlaute grundsätzlich erlaubt sind, sollten diese unbedingt vermieden werden (ü -> ue, ä -> ae etc.)
* Zahlen dürfen nicht am Anfang eines Bezeichners stehen

Variablen kann ein Wert zugewiesen werden.

Dies erfolgt über den Zuweisungsoperator `=`

Variablen können im Laufe des Programms verschiedene Werte annehmen.

### Zuweisung:

Die gesamte Zeile bezeichnet man als *Ausdruck*:

```
meine_variable = "wert"     
```

* `meine_variavle` ist der *Bezeichner*
* `=` ist der *Zuweisungsoperator*
* `"wert"` ist ein *String Literal*

Variablen können aber nicht nur einzelne feststehende Werte aufnehmen, sondern auch ganze Ausdrücke:

```
ergebnis = 3 + 5
```

Diese Ausdrücke können natürlich auch selbst Variablen enthalten, man kann also Variablen 
anderen Variablen zuweisen:

```
ergebnis = zahl + nummer * 3
```

Auch die Rückgabe/das Ergebnis einer Funktion kann in einer Variable gespeichert werden:

```
user_input = input("Bitte etwas eingeben: ")
laenge_input_string = len(usr_input)
```

## Datentypen

Ein Datentyp gibt an, um welche Art von Daten es sich handelt, also wie die entsprechende
Datenstruktur aufgebaut ist und welche Operationen man mit diesen Daten (in Python sind dies
*Objekte*) durchführen kann.

In Python gibt es unter anderem folgende Datentypen:

Name            | Bezeichnung   | in Python
----------------|---------------|-----------
Ganze Zahl      | *Integer*     | `int`
Gleitkommazahl  | *Float*       | `float`
Zeichenkette    | *String*      | `str`
Wahrheitswert   | *Boolean*     | `bool`

Eine Variable enthält immer einen bestimmten Datentyp, z.B. einen Integer, einen String etc.

## Beispiele für Zuweisungen und Datentypen:

```
ganze_zahl = 8         # 8 ist ein Integer (ganze Zahl)
komma_zahl = 3.234     # 3.234 ist ein Float (Gleitkommazahl)
                       # hier ist der Punkt (.) der Dezimaltrenner und nicht das Komma (,)
text = "irgendwas"     # "irgendwas" ist ein String (Zeichenkette)
wahrheitswert = True   # True ist ein Boolean (Wahrheitswert: entweder True (wahr) oder False (falsch)
```

## Casting

Mittels *Casting* kann ein Datentyp bei Bedarf in einen anderen umgewandelt werden. 

Dies funktioniert nicht immer, die Datentypen müssen hierfür zusammen "passen".

### Casting von int zu float:

```
mein_int = 5
print(mein_int)
>>> 5
print(type(mein_int))
>>> <class 'int'>

mein_float = float(mein_int)
print(mein_float)
>>> 5.0
print(type(mein_float))
>>> <class 'float'>
```

### Casting von int zu String:

```
mein_string = str(mein_int)
print(mein_string)
>>> '5'
print(type(mein_float))
>>> <class 'str'>
```

Folgendes geht aber z.B. nicht:

```
mein_satz = "Ich kann nicht in einen Integer gecastet werden"
int_satz = int(mein_satz)  # -> führt zu einem Fehler im Programm
>>> Traceback (most recent call last):
>>>   File "<input>", line 1, in <module>
>>> ValueError: invalid literal for int() with base 10: 'Ich kann nicht in einen Integer gecastet werden'
```

Den Datentyp kann man mit dem *Builtin* `type()` ermitteln:

```
print(type(mein_string))
>>> <class 'str'>
```

Dies ist ein *Debuggingstatement* -> wichtig zur Codeanalyse/Fehlersuche!

## Builtins / Funktionen:

* sind in Python eingebaute und direkt verfügbare Funktionen
* können unabhängig von einem *Objekt* verwendet werden

# Beispiele:

```
print()
input()
type()
len()
int()
float()
...
```

*Builtins* nehmen *Parameter (Argumente)* entgegen. Diese werden von der Funktion verarbeitet 
(*EVA* Prinzip).

Inhalt von `mein_satz` ausgeben:
```
print(mein_satz)         # mein_satz ist der Parameter/das Argument
```
Länge des Strings `mein_string` ermitteln (aber nicht ausgeben!):

```
len(mein_string)         # mein_string ist der Parameter/das Argument
```

Länge des Strings `mein_string` ermitteln und ausgeben:

```
print(len(mein_string))  # Länge von mein_string ermitteln UND ausgeben
```

## Stringmethoden

Methoden können im Gegensatz zu Funktionen nicht einfach so aufgerufen werden, sie werden über die Punktnotation 
durch ein Objekt aufgerufen:

```
mein_string.upper()     # alle Buchstaben GROSS schreiben
mein_string.lower()     # alle Buchstaben klein schreiben
```

In *IDLE* oder *PyCharm* kann man sich die verfügbaren Methoden anzeigen lassen, indem man hinter ein Objekt einen Punkt 
schreibt und in *IDLE* `STRG+SPACE` drückt. In *PyCharm* passiert das nach einer kurzen Wartezeit automatisch.

Folgendes geht nicht:
```
upper(mein_string)    
```
Das geht so nicht, denn `upper()` ist eine Methode der Klasse *String* und keine Funktion oder Builtin.

Es gibt natürlich nicht nur String Methoden, sondern jede Klasse in Python hat ihre eigenen Methoden implementiert.

## String Indexing

Über *Indexing* kann auf ein einzelnes Element (in diesem Fall ein Buchstabe) des String Objekts zugegriffen werden:

```
mein_string = 'Python'
print(mein_string[0])
>>> P

print(mein_string[3])
>>> h
```

Wir können aber auch von hinten anfangen zu zählen:

```
print(mein_string[-1])
>>> n

print(mein_string[-3])
>>> h
```

Beim Versuch, auf einen Index zuzugreifen der nicht existiert, kommt es zu einem Fehler/einer Exception:
```
print(mein_string[10])
# FEHLER: Index out of range Exception
```

WICHTIG: Computer fangen in der Regel bei 0 an zu zählen!

Die einzelnen Elemente (eines iterierbaren Objekts) werden über ihren *Index* angesprochen.

Der Index startet immer bei 0.

Oben wird der Index in die eckigen Klammern `[]` geschrieben.


## String Slicing

Mittels Slicing kann eine Abfolge von Elementen (Buchstaben) aus einem String ausgeschnitten werden.

Syntax: `str[start:ende]`

`start` ist inklusive (wird also mit ausgegeben).

`ende` ist exklusive (wird nicht mit ausgegeben).

```
mein_string = "Slicing"
# Index:       0123456

print(mein_string[0:3])    # Achtung: Indes 3, das 'c' ist exklusive/nicht enthalten!
>>> 'Sli'

print(mein_string[:1])
>>> 'S'

print(mein_string[4:6])
>>> 'in'
```

Liegt das Ende aussehalb des Bereichs, kommt es nicht zu einem Fehler.

Dies ist ein wichtiger Unterschied zum Indexing (s.o.):

```
print(mein_string[4:600])
>>> 'in'
```

Die obere oder untere Grenze kann auch weggelassen werden:

```
print(mein_string[4:])
>>> 'in'
```

## Verzweigungen - If-Statements

Dienen dazu, den Programmablauf / Flow zu steuern.

Das Schlüsselwort/Keyword `if` leitet einen Programmabschnitt ein, der nur unter einer bestimmten Bedingung ausgeführt 
wird.

```
zahl = 5
if zahl < 10:                              # Bedingung ist wahr/liefert True zurück
    print(f"{zahl} ist kleiner als 10")    # Codeblock wird ausgeführt
    print("Ich gehöre mit zum Codeblock")
>>> 5 ist kleiner als 10
>>> Ich gehöre mit zum Codeblock

if zahl > 10:                              # Bedingung ist falsch/liefert False zurück
    print(f"{zahl} ist kleiner als 10")    # Codeblock wird nicht ausgeführt
    print("Ich gehöre mit zum Codeblock")
>>>                                        # keine Ausgabe, nichts passiert
```

Syntax:

```
if Bedingung:
    auszuführender Codeblock
    über beliebige 
    viele Zeilen
    mit der gleichen Einrückung
```

### else

```
zahl = 5
if zahl > 10:                              # Bedingung ist falsch/liefert False zurück
    print(f"{zahl} ist kleiner als 10")    # Codeblock wird nicht ausgeführt
    print("Ich gehöre mit zum Codeblock")
else:                                      # dafür aber dieser hier
    print("Ich werde nur ausgegeben, wenn die Bedingung falsch ist")
>>> Ich werde nur ausgegeben, wenn die Bedingung falsch ist
```

### elif   ("else if" abgekürzt)

```
zahl = -1
if zahl > 0:                              # Bedingung ist falsch/liefert False zurück
    print(f"{zahl} ist positiv")          # Codeblock wird nicht ausgeführt
    print("Ich gehöre mit zum Codeblock")
elif zahl < 0:                            # diese Bedingung ist wahr
    print(f"{zahl} ist negativ")          # Codeblock wird ausgeführt
else:                                     # da elif Block wahr, wird else Block nicht ausgeführt
    print(f"{zahl} ist Null")             # Codeblock wird nicht ausgeführt
```


## Codeblock / Indentation

Codeblöcke werden in Python ausschließlich durch Einrückungen gekennzeichnet, nicht wie in anderen Programmiersprachen 
durch z.B. geschweifte Klammern `{}`.

Beispiel Java:

```
if(zahl > 0) {
  println("Zahl ist positiv")
  println("Ich gehöre mit zum Codeblock")
}
```

Beispiel Python:

```
if zahl > 0:
    print("Zahl ist positiv")
    print("Ich gehöre mit zum Codeblock")
```

Codeblöcke werden standardmäßig um 4 Leerschritte eingerückt.

Eine Einrücktiefe von 2 Leerschritten ist auch verbreitet und ebenso okay.

Obwohl auch Einrücktiefen von z.B. 3 theoretisch möglich sind, ist dringend davon abzuraten!

In jedem Fall muss die Einrücktiefe innerhalt eines Blocks gleich sein. 

Generell sollte man sich für eine Einrücktiefe entscheiden und dabei bleiben.


## String Konkatenation

Um mehrere Strings oder Strings und Variablen miteinander zu verbinden, kann z.B. die String-Konkatenation genutzt werden.

Hierbei dient das `+` Zeichen als Verbindungsoperator.

Wir möchten den String "Hallo Peter" ausgeben:

```
name = "Peter"
print("Hallo " + name)
>>> 'Hallo Peter'
```

Dies ist eine einfache Art, Variabeln und Strings zu verknüpfen, allerdings etwas umständlich und fehleranfällig:

```
name = "Peter"
alter = 23

# Wir wollen folgenden String ausgeben "Hallo Peter, du bist 23 Jahre alt":
print("Hallo " + name + " du bist " + alter)     # FEHLER!
>>> TypeError: can only concatenate str (not "int") to str
```

### Lösungen:

Zahl als String repräsentieren: `alter = '23'`

Schwachstellt dabei: Wir könnten damit nicht rechnen.

Den Integer in einen String zu casten ist die bessere Lösung:

```
name = "Peter"
alter = 23
print("Hallo " + name + " du bist " + str(alter))     # so funktioniert es
```

### F-String

F-Stings sind die übersichtlichste und komfortabelste Art, formatierte Strings auszugeben oder Strings und Variablen 
zu verknüpfen. Hier muss in diesem Fall nicht selbst gecastet werden:

```
name = "Peter"
alter = 23
print(f"Hallo {name} du bist {alter}")
```

## Funktionen erstellen

Funktionen dienen dazu:
* einzelne Programmteile zusammenzufassen
* diese können dann an anderer Stelle (auch mehrfach) aufgerufen werden
* der Code wird dadurch strukturierter/übersichtlicher
* Redundanzen (Wiederholungen) können so vermieden werden
* Code kann wiederverwendet werden
* Funktionen kann man als soetwas wie ein "Unterprogramm" verstehen

Funktionen werden durch das Schlüsslewort `def` eingeleitet.

```
# Funkionsdefinition / Funkionsdeklaration
def sag_hallo():
    print("Hallo")

# Funkionsaufruf
sag_hallo()
>>> 'Hallo'
```

Durch Parameter/Argumente kann eine Funktion variabler werden:

```
# Funkionsdeklaration
def sag_hallo(name):
    print(f"Hallo {name}")

# Funkionsaufruf
sag_hallo('Peter')
>>> 'Hallo Peter'
```

Funktionen müssen definiert / deklariert werden. Um sie aber zu nutzen, müssen sie zusätzlich aufgerufen werden.

Wird eine Funktion so deklariert, dass sie eine bestimmte Anzahl an Parametern entgegennimmt, so muss die Funktion 
auch mit exakt dieser Anzahl an Parametern aufgerufen werden.

Es gibt auch Funktionen, bei denen dies anders ist, die also z.B. eine beliebige Anzahl an Parametern entgegennehmen 
können. Dies muss aber bei der Funktionsdeklaration entsprechend mit einer bestimmten Syntax angegeben werden.

## Schleifen / Loops

Schleifen führen einen bestimmten Codeblock mehrfach bis zum Eintreten einer sog. Abbruchbedingung aus.

In Python gibt es zwei Arten von Schleifen: Die `while` und die `for` Schleife.

### While Schleife
```
x = 110
while x < 10:             # x < 10 ist die zu prüfende Bedingung
    print(x, sep=" ")     # dieser Block wird wiederholt ausgeführt
    x = x + 1             # Wichtig, damit wir keine Endlosschleife bauen! -> Inkrement
#   x += 1                # ist der gleiche Ausdruck wie eine Zeile darüber

>>> 0 1 2 3 4 5 6 7 8 9
```

`sep=" "` sorgt dafür, dass `print` keine Zeilenumbruch durchführt, sondern anstatt dessen ein Leerzeichen einfügt.

Bei der *while* Schleife ist es sehr wichtig darauf zu achten, dass die Abbruchbedingung auch eintritt.
Ansonsten kommt es zu einer sog. Endlosschleife, der Schleifenrumpf wird also theoretisch unendlich oft ausgeführt 
und das Programm bleibt "hängen" oder stürzt sogar ab.

Endlosschleifen können unter bestimmten Bedingungen aber auch erwünscht sein, z.B. für eine wiederholte Aufforderung zur 
Benutzereingabe etc. zu erreichen.

Hier gibt es dann andere Möglickkeiten, die Schleife zu verlassen (`break`, `continue`).

### For Schleife

Die `for` Schleife kann nur auf sog. *Iterables*, also iterierbare Objekte angewandt werden. Damit sind Datenstrukturen 
gemeint, die mehrere Elemente enthalten, wie z.B. ein String, eine List etc.

Bei einer for-Schleife muss nicht selbst darauf geachtet werden, dass die Abbruchbedingung eintritt, die Schleife "weiß" 
von selbst, wann sie aufhören muss.

Alles, was mit einer `for` Schleife geht, ist auch mit einer `while` Schleife möglich, die `for` Schleife ist in vielen 
Fällen aber komfortabler und kürzer.

```
for letter in "Python":
    print(letter)

>>> P
>>> y
>>> t
>>> h
>>> o
>>> n
```

`letter` ist hier ein frei gewählter Bezeichner, über den das entsprechende Element (also pro Schleifendurchlauf immer 
das nächstfolgende Element) innerhalb des Rumpfs angesprochen/genutzt werden kann.

Eine *Zählschleife* kann über die Funktion `range()` realisiert werden:

```
for num in range(1, 6):
    print(num, sep=", ")

>>> '1, 2, 3, 4, 5'
```

Genau wie beim *Slicing* ist auch bei `range()` der Start inklusive und das Ende exklusive.

## Exceptions

## Lists