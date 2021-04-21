# Funktionsdefinition (es gibt diese Funktion mit entsprechender Funktionalität)
def convert_days(num_of_days):   # Kopf einer Funktion / Signatur
    """Convert given number of days to hours."""
    conversion = num_of_days * 24
    # F-String (Formatierter String)
    print(f"{num_of_days} Tage sind {conversion} Stunden")


def validate_and_execute():
    """Validate if user_input is a valid number. Throw an exception if not.
    Print detailed error message."""
    try:                                      # Exception
        user_input_number = int(user_input)   # Umwandlung input in Integer
        if user_input_number > 0:             # Test, ob eingegebenen Zahl positiv
            convert_days(user_input_number)   # Funktionsaufruf convert_days()
        elif user_input_number == 0:          # Test, ob eingegebene Zahl 0g
            print("Du hast 0 eingegeben. So funktioniert das nicht!")
        else:
            print("Es muss eine positive Zahl eingegeben werden.")
    except ValueError:
        print("Eingabe war keine gültige Zahl. Mach doch sowas nicht.")

# Logik
# Funktionsaufruf / Call the function
user_input = None                 # leere Variable user_input erzeugen

while user_input != "exit":     # Endlosschleife, mit STRG+C beenden
    user_input = input("Anzahl der Tage eingeben, die dann in Stunden umgewandelt werden: ")
    validate_and_execute()
