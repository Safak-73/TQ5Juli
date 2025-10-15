# paketversand_system.py

class Paket:
    def __init__(self, paketID: int, gewicht: float, zielort: str, versichert: bool):
        if gewicht < 0:
            raise ValueError("Gewicht darf nicht negativ sein!")
        self.paketID = paketID
        self.gewicht = gewicht
        self.zielort = zielort
        self.versichert = versichert

    def berechne_versandkosten(self) -> float:
        basispreis = 5
        kosten = basispreis + self.gewicht * 1
        if self.versichert:
            kosten += 2
        return kosten

    def __str__(self):
        versichert_text = "Ja" if self.versichert else "Nein"
        return (f"Paket-ID: {self.paketID} | Gewicht: {self.gewicht} kg | "
                f"Ziel: {self.zielort} | Versichert: {versichert_text} | "
                f"Kosten: {self.berechne_versandkosten():.2f} €")


class Paketverwaltung:
    def __init__(self):
        self.pakete = []

    def paket_hinzufuegen(self, p: Paket):
        self.pakete.append(p)

    def alle_anzeigen(self):
        for p in self.pakete:
            print(p)

    def gesamt_kosten(self) -> float:
        return sum(p.berechne_versandkosten() for p in self.pakete)

    def exportiere_datei(self, dateiname: str):
        with open(dateiname, "w", encoding="utf-8") as f:
            for p in self.pakete:
                f.write(f"{p.paketID};{p.gewicht};{p.zielort};{p.versichert}\n")
        print(f"Daten erfolgreich in '{dateiname}' gespeichert.")

    def importiere_datei(self, dateiname: str):
        try:
            with open(dateiname, "r", encoding="utf-8") as f:
                for zeile in f:
                    daten = zeile.strip().split(";")
                    if len(daten) == 4:
                        paketID = int(daten[0])
                        gewicht = float(daten[1])
                        zielort = daten[2]
                        versichert = daten[3] == "True"
                        self.paket_hinzufuegen(Paket(paketID, gewicht, zielort, versichert))
        except FileNotFoundError:
            print(f"Datei '{dateiname}' nicht gefunden. Neue Liste wird erstellt.")


def main():
    verwaltung = Paketverwaltung()
    dateiname = "pakete.txt"
    verwaltung.importiere_datei(dateiname)

    # Beispielpakete hinzufügen
    try:
        p1 = Paket(101, 3.5, "Berlin", True)
        p2 = Paket(102, 2.0, "Hamburg", False)
        verwaltung.paket_hinzufuegen(p1)
        verwaltung.paket_hinzufuegen(p2)
    except ValueError as e:
        print(f"Fehler beim Hinzufügen eines Pakets: {e}")

    verwaltung.alle_anzeigen()
    print(f"Gesamtkosten: {verwaltung.gesamt_kosten():.2f} €")

    verwaltung.exportiere_datei(dateiname)


if __name__ == "__main__":
    main()
