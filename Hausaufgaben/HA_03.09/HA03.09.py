import os

def projekt_fragen_ausgeben(dateiname: str = "ProjektFragen.txt") -> str:
    """
    Öffnet die Datei mit den Projektfragen (im selben Ordner wie dieses Skript)
    und gibt den Inhalt nummeriert als String zurück.

    Args:
        dateiname (str, optional): Dateiname. Standard ist "ProjektFragen.txt".

    Returns:
        str: Nummerierte Fragen oder eine Fehlermeldung.
    """
    # Ordner, in dem dieses Skript liegt
    ordner = os.path.dirname(__file__)
    pfad = os.path.join(ordner, dateiname)

    try:
        with open(pfad, "r", encoding="utf-8") as f:
            inhalt = f.readlines()
        return "".join([f"{i+1}. {zeile}" for i, zeile in enumerate(inhalt)])
    except FileNotFoundError:
        return f"Datei '{dateiname}' nicht gefunden im Ordner {ordner}."


# Testaufruf (nur wenn Skript direkt gestartet wird)
if __name__ == "__main__":
    print(projekt_fragen_ausgeben())

