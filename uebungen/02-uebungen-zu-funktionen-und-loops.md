
# Table of Contents

1.  [Übungen Zu Funktionen Und Loops](#orgc27c743)
2.  [Funktionen](#org1fcf107)
3.  [Loops](#org4a1dacf)



<a id="orgc27c743"></a>

# Übungen Zu Funktionen Und Loops


<a id="org1fcf107"></a>

# Funktionen

1.  Schreibt ein Programm mit Namen `temperature-converter.py`, welches zwei Funktionen definiert:
    -   `convert_cel_to_far()`, welche einen Float-Parameter (Temperatur in Celsius) entgegennimmt und einen `float` zurückgibt, der die gleiche Temperatur in Fahrenheit ausgibt. Nutzt dazu die Formel `F = C * 9/5 + 32`.
    -   `convert_far_to_cell()`, welche obige Umwandlung von Fahrenheit in Celsius vornimmt. Nutzt dazu folgende Formel: `C = (F - 32) * 5/9`
2.  Das Programm soll die Ergebnisse auf zwei Nachkommastellen gerundet angeben (Nutzt entweder `round()` oder die Formatierung in einem F-String). Die Ausgabe könnte wie folgt aussehen:
    
        Bitte einen Temperatur in Grad Celsius angeben: 37
        37 Grad Celsius sind 98.60 Grad Fahrenheit
        
        Bitte eine Temperatur in Grad Fahrenheit angeben: 72
        72 Grad Fahrenheit sind 22.22 Grad Celsius


<a id="org4a1dacf"></a>

# Loops

1.  Schreibt einen `for` Loop, der alle Integer zwischen 2 und 10 ausgibt, jeden auf einer neuen Zeile. Nutzt dafür `range()`
2.  Macht das gleiche nun mit einem `while` Loop.
3.  Schreibt einen Funktion mit dem Namen `doubles()`, welche eine Ganzzahl entgegennimmt und diese verdoppelt. Nutzt anschliessend diese Funktion `doubles()` in einem Loop, welcher die übergebene Zahl drei Mal verdoppelt. Mit der Zahl 2 würde folgendes ausgegeben werden:
    
        4
        8
        16

