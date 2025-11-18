# Benutzer nach Eingabe fragen
jahr = int(input("Bitte ein Jahr eingeben: "))

# Überprüfung, ob Schaltjahr oder nicht
if jahr % 400 == 0:
    print(f"Das Jahr {jahr} ist ein Schaltjahr.")
elif jahr % 100 == 0:
    print(f"Das Jahr {jahr} ist kein Schaltjahr.")
elif jahr % 4 == 0:
    print(f"Das Jahr {jahr} ist ein Schaltjahr.")
else:
    print(f"Das Jahr {jahr} ist kein Schaltjahr.")
