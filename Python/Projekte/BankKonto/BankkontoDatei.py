from KundeDatei import Kunde
from random import randint
from datetime import datetime

class Bankkonto:
    """Repräsentiert ein Bankkonto mit Kontoinhaber, Kontonummer, PIN und Transaktionshistorie."""

    def __init__(self, kontoinhaber:Kunde, kontonummer, startguthaben=0):
        """Initialisiert ein neues Bankkonto.

        Args:
            kontoinhaber (Kunde): Der Kontoinhaber.
            kontonummer (str): Die Kontonummer.
            startguthaben (float, optional): Startguthaben. Defaults to 0.
        """
        self.kontoinhaber = kontoinhaber
        self.kontostand = startguthaben
        self.kontonummer = kontonummer
        self.pin = Bankkonto.pin_generator()
        self.transaktions_historie = []

    def pin_generator():
        """Generiert eine zufällige 4-stellige PIN.

        Returns:
            str: Die generierte PIN.
        """
        neues_pin = ''
        for i in range(0,4):
            neues_pin += str(randint(0,9))
        print('Das neue Pin ist:',neues_pin)
        return neues_pin

    def details(self):
        """Gibt die Details des Bankkontos aus."""
        print('=======================================')
        print(f'Kontoinhaber: {self.kontoinhaber.detail_kunde(False)}')
        print(f'Kontonummer: {self.kontonummer}\nKontostand: {self.kontostand}')
        print('=======================================')

    def einzahlen(self, betrag):
        """Zahlt einen Betrag auf das Konto ein.

        Args:
            betrag (float): Der einzuzahlende Betrag.

        Returns:
            bool: True bei Erfolg, False bei ungültigem Betrag.
        """
        if betrag <= 0:
            print('0 und Negative Betraege sind nicht erlaubt.')
            return False
        self.kontostand += betrag
        self.transaktions_historie.append(('Einzahlen',betrag,self.kontostand,datetime.now()))
        print('Einzahlung erfolgreich.')
        return True
        
    def auszahlen(self, betrag):
        """Zahlt einen Betrag vom Konto aus.

        Args:
            betrag (float): Der auszuzahlende Betrag.

        Returns:
            bool: True bei Erfolg, False bei ungültigem Betrag.
        """
        if betrag <= 0:
            print('0 und Negative Betraege sind nicht erlaubt.')
            return False
        self.kontostand -= betrag
        self.transaktions_historie.append(('Auszahlen',betrag,self.kontostand,datetime.now()))
        print('Auszahlung erfolgreich')
        return True
    
    def einkommende_ueberweisung(self, betrag, kontonummer):
        """Verarbeitet eine eingehende Überweisung.

        Args:
            betrag (float): Der überwiesene Betrag.
            kontonummer (str): Die Kontonummer des Absenders.
        """
        self.kontostand += betrag
        self.transaktions_historie.append((f'Einkommende Ueberweisung von: {kontonummer}',betrag,self.kontostand,datetime.now()))
    
    def ausgehende_ueberweisung(self, betrag, kontonummer):
        """Verarbeitet eine ausgehende Überweisung.

        Args:
            betrag (float): Der überwiesene Betrag.
            kontonummer (str): Die Kontonummer des Empfängers.
        """
        self.kontostand -= betrag
        self.transaktions_historie.append((f'Ausgehende Ueberweisung an: {kontonummer}',betrag,self.kontostand,datetime.now()))

    def kontostand_ansehen(self):
        """Gibt den aktuellen Kontostand aus."""
        print('Dein Aktueller Kontostand betraegt:',self.kontostand)

    def kontoauszug(self):
        """Gibt die Transaktionshistorie des Kontos aus."""
        print('==========Transaktionshistorie==========')
        print('(operation,betrag,kontostand,timestamp)')
        for eintrag in self.transaktions_historie:
            print(eintrag)
        print('==========EndeHistorie==========')