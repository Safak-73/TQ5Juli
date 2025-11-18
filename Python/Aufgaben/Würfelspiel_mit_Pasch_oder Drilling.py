from random import randint

import time

# Liste für die Übersicht ( )
alle_ergebnisse = []

for i in range(10):  # 3 komplette Würfe
    print(f"\nRolling the dice... Wurf {i+1}")

    w1 = randint(1, 6)
    w2 = randint(1, 6)
    w3 = randint(1, 6)

    print("You rolled:", w1, w2, w3, "=> Summe:", (ergebnis := w1 + w2 + w3))

    if w1 == w2 == w3:
        bonus = 6
        print("and got a bonus of", bonus)
    elif w1 == w2 or w2 == w3 or w1 == w3:
        bonus = 2
        print("and got a bonus of", bonus)
    else:
        bonus = 0

    gesamt = ergebnis + bonus
    print("Your total score is", gesamt)

    if gesamt >= 15:
        preis = "Cat :3!"
    elif gesamt >= 10:
        preis = "Dog :3!"
    elif gesamt >= 7:
        preis = "Hamster :3!"
    else:
        preis = "Nothing :("

    print("You won:", preis)

    # Ab hier mit hilfe von der KI, um die Ergebnisse zu speichern und auszugeben
    

 # Speichere das Ergebnis für die Übersicht
    alle_ergebnisse.append({
        "Wurf": i + 1,
        "Würfel": (w1, w2, w3),
        "Summe": ergebnis,
        "Bonus": bonus,
        "Gesamt": gesamt,
        "Gewinn": preis
    })

print("Loading results...")
time.sleep(5)  # Simuliere eine Ladezeit
print("Results loaded successfully!")

# ---------------------------
# Übersicht am Ende
# ---------------------------
print("\n===== Gesamtübersicht =====")
gesamtpunkte = 0
for eintrag in alle_ergebnisse:
    print(f"Wurf {eintrag['Wurf']}: Würfel {eintrag['Würfel']} "
          f"=> Summe {eintrag['Summe']} + Bonus {eintrag['Bonus']} "
          f"= {eintrag['Gesamt']} | Gewinn: {eintrag['Gewinn']}")
    gesamtpunkte += eintrag["Gesamt"]

print("\nGesamtpunkte aus allen Würfen:", gesamtpunkte)