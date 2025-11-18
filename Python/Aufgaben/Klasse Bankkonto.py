class Bankkonto:
    """Repräsentiert ein Bankkonto.

    Attribute:
        kontonummer (str): Die eindeutige Kontonummer.
        inhaber (str): Name des Kontoinhabers.
        guthaben (float): Aktuelles Guthaben des Kontos.
        waehrung (str): Währung des Kontos, Standard ist "EUR".
        bankname (str): Name der Bank (hartcodiert: "Musterbank").
    """

    def __init__(self, kontonummer: str, inhaber: str, startguthaben: float = 0.0, waehrung: str = "EUR"):
        """Initialisiert ein neues Bankkonto.

        Args:
            kontonummer (str): Die eindeutige Kontonummer.
            inhaber (str): Name des Kontoinhabers.
            startguthaben (float, optional): Startguthaben beim Erstellen des Kontos.
                Standardwert ist 0.0.
            waehrung (str, optional): Währung des Kontos. Standardwert ist "EUR".
        """
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.guthaben = startguthaben
        self.waehrung = waehrung
        self.bankname = "Musterbank"

    def details(self) -> None:
        """Gibt die Kontodetails auf der Konsole aus.

        Returns:
            None
        """
        print("---- Kontodetails ----")
        print(f"Bank: {self.bankname}")
        print(f"Inhaber: {self.inhaber}")
        print(f"Kontonummer: {self.kontonummer}")
        print(f"Guthaben: {self.guthaben:.2f} {self.waehrung}")
        print("----------------------")

