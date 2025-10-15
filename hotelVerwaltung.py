# hotelreservierung_system.py

class Gast:
    def __init__(self, gastID: int, name: str, email: str):
        self.gastID = gastID
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} (ID: {self.gastID}, E-Mail: {self.email})"


class Zimmer:
    def __init__(self, zimmernummer: int, preis_pro_nacht: float, belegt: bool = False):
        self.zimmernummer = zimmernummer
        self.preis_pro_nacht = preis_pro_nacht
        self.belegt = belegt

    def __str__(self):
        status = "Belegt" if self.belegt else "Frei"
        return f"Zimmer {self.zimmernummer} | {status} | Preis/Nacht: {self.preis_pro_nacht:.2f} €"


class Reservierung:
    def __init__(self, reservierungsID: int, gast: Gast, zimmer: Zimmer, anzahl_naechte: int):
        self.reservierungsID = reservierungsID
        self.gast = gast
        self.zimmer = zimmer
        self.anzahl_naechte = anzahl_naechte

    def berechne_kosten(self) -> float:
        return self.zimmer.preis_pro_nacht * self.anzahl_naechte

    def __str__(self):
        return (f"Gast: {self.gast.name} | Zimmer: {self.zimmer.zimmernummer} | "
                f"Nächte: {self.anzahl_naechte} | Kosten: {self.berechne_kosten():.2f} €")


class HotelVerwaltung:
    def __init__(self):
        self.gaeste = []
        self.zimmer = []
        self.reservierungen = []

    def gast_hinzufuegen(self, gast: Gast):
        self.gaeste.append(gast)

    def zimmer_hinzufuegen(self, zimmer: Zimmer):
        self.zimmer.append(zimmer)

    def reservierung_erstellen(self, gastID: int, zimmernummer: int, naechte: int):
        gast = next((g for g in self.gaeste if g.gastID == gastID), None)
        zimmer = next((z for z in self.zimmer if z.zimmernummer == zimmernummer), None)

        if gast is None:
            print(f"Fehler: Kein Gast mit ID {gastID} gefunden!")
            return

        if zimmer is None:
            print(f"Fehler: Kein Zimmer mit Nummer {zimmernummer} gefunden!")
            return

        if zimmer.belegt:
            print(f"Fehler: Zimmer {zimmernummer} ist bereits belegt!")
            return

        reservierungsID = len(self.reservierungen) + 1
        neue_res = Reservierung(reservierungsID, gast, zimmer, naechte)
        self.reservierungen.append(neue_res)
        zimmer.belegt = True
        print("Reservierung erfolgreich erstellt!")
        print(neue_res)

    def zeige_reservierungen(self):
        if not self.reservierungen:
            print("Keine Reservierungen vorhanden.")
        else:
            print("\nAktuelle Reservierungen:")
            for r in self.reservierungen:
                print(r)


def main():
    hotel = HotelVerwaltung()

    # Gäste hinzufügen
    hotel.gast_hinzufuegen(Gast(1, "Max Mustermann", "max@example.com"))
    hotel.gast_hinzufuegen(Gast(2, "Anna Schmidt", "anna@example.com"))

    # Zimmer hinzufügen
    hotel.zimmer_hinzufuegen(Zimmer(101, 90.0))
    hotel.zimmer_hinzufuegen(Zimmer(102, 100.0))
    hotel.zimmer_hinzufuegen(Zimmer(103, 80.0))

    # Reservierungen erstellen
    hotel.reservierung_erstellen(1, 101, 3)
    hotel.reservierung_erstellen(2, 101, 2)  # sollte Fehler geben (Zimmer belegt)
    hotel.reservierung_erstellen(2, 102, 2)

    # Reservierungen anzeigen
    hotel.zeige_reservierungen()


if __name__ == "__main__":
    main()
