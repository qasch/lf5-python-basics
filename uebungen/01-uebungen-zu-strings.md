
# Table of Contents

1.  [Strings](#orgef9658b)
    1.  [Stringmethoden](#org59159d3)
    2.  [Strings and Numbers](#org092957b)



<a id="orgef9658b"></a>

# Strings

1.  Erstellt einen String und gebt anschliessend mit der `len()` Funktion dessen Länge aus.
2.  Erzeugt zwei Strings, verbindet (*konkateniert*) sie mit dem `+` Operator und gebt den resultierenden String aus.
3.  Erzeugt zwei Strings, verbindet sie mit einem Leerzeichen dazwischen und gebt das Ergebnis aus.
4.  Extrahiert den String `zing` mittels *Slicing* aus dem String `bazinga`.
5.  Gegeben sei der absolute Pfad &ldquo;D:\backup\documents\python-examples\string-slicing.py&rdquo;. Schneidet mittels *Slicing* lediglich den Namen des Python Skripts `sting-slicing.py` aus. Speichert den resultierenden *Substring* in einer Variable. Erzeugt zwei weitere Variablen `datei_name` und `datei_endung` und speichert den Dateinamen ohne Dateierweiterung (`.py`) in `datei_name` und die Dateierweiterung `.py` in der Variablen `datei_endung`.


<a id="org59159d3"></a>

## Stringmethoden

1.  Schreibt ein Programm, dass die folgenden Strings komplett in Grossbuchstaben umwandelt:
    -   &ldquo;Pinguin&rdquo;, &ldquo;Affenfalter&rdquo;, &ldquo;Pommes mit Sahne&rdquo;
2.  Wiederholt die vorige Aufgabe, nur dass ihr diesmal alle Strings in Kleinbuchstaben ausgent.
3.  Schreibt ein Programm, dass alle *Whitespaces* (in diesem Fall Leerzeichen) von den folgenden Strings entfernt. Schaut euch dazu die Stingmethoden `rstrip()`, `lstrip()` und `strip()` an.
    
        string1 = "     Pommes Schranke"
        string2 = "Currywurst     "
        string3 = "    Veggieburger    "
4.  Schreibt ein Programm, dass das Ergebnis von `.startswith("be")` für jeden der folgenden Strings ausgibt:
    
        string1 = "Becomes"
        string2 = "becomes"
        string3 = "BEAR"
        string1 = "   bEautiful"

5.  Schreibt nun ein Programm, welches Stringmethoden gebraucht, um jeden der obigen Strings so umzuwandeln, dass `startswith("be") =True` für alle Strings zurückgibt.


<a id="org092957b"></a>

## Strings and Numbers

1.  Erstellt einen String, welcher eine Ganzzahl enthält und wandelt ihn anschliessend in ein *echtes* Integer Objekt um mit der `int()` Funktion. Testet euer Ergebnis, indem ihr euer String Objekt mit einem weiteren Integer multipliziert.
2.  Wiederholt obige Übung mit einer Gleitkommazahl/Float.
3.  Erzeugt einen Integer und einen Float und gebt beide hintereinander (mit Leerzeichen dazwischen) in einem(!) String Statement aus.
4.  Schreibt ein Programm, welches mit zwei `input()` nach zwei Zahlen fragt, diese miteinander multipliziert und das Ergebnis ausgibt.
    Sind die beiden Zahlen z.B. 2 und 4, sollte das Programm folgendes ausgeben:
    
        Das Produkt von 2 und 4 ist 8.0

