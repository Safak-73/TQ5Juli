from random import randint


class Bank:
    '''Bank-Klasse zur Verwaltung von Kunden und Konten'''
    def __init__(self, name:str, hauptstandort:str, region:str, land:str):
        """
        Initialisiert eine neue Bankinstanz mit Name, Hauptstandort, Region und Land.
        Erstellt leere Listen für Konten und Kunden.
        """
        self.kontos:list[Bankkonto] = []
        self.kunden:list[Kunde] = []
        self.name = name
        self.hauptstandort = hauptstandort
        self.region = region
        self.land = land

    def geld_ueberweisung(self,von_kontonummer:str,zu_kontonummer:str,betrag:float):
        """
        Führt eine Geldüberweisung zwischen zwei Konten durch.
        Überprüft die Existenz beider Kontonummern und die Gültigkeit des Betrags.
        Gibt True bei Erfolg, sonst False zurück.
        """
        #Schaue ob "von_kontonummer" existiert. Wenn nicht. Ist die geld_ueberweisung nicht erfolgreich
        von_gesuchter_konto = self.bankkonto_finden(von_kontonummer)
        if von_gesuchter_konto[0] == False:
            print('Ungueltige "von Kontonummer" eingegeben.')
            return False
        
        #Schaue ob "zu_kontonummer" existiert. Wenn nicht. Ist die geld_ueberweisung nicht erfolgreich
        zu_gesuchter_konto = self.bankkonto_finden(zu_kontonummer)
        if zu_gesuchter_konto[0] == False:
            print('Ungueltige "zu Kontonummer" eingegeben.')
            return False
        
        #Schaue ob der Betrag eine Positive Zahl ist. Wenn nicht. Ist die geld_ueberweisung nicht erfolgreich        
        if betrag<=0:
            print('Ungueltiger Betrag. Nur Positive Zahlen eingeben groesser 0.')
            return False
        
        von_gesuchter_konto[1].ausgehende_ueberweisung(betrag,zu_kontonummer)
        zu_gesuchter_konto[1].einkommende_ueberweisung(betrag,von_kontonummer)
        return True


    def bankkonto_finden(self, gesuchte_kontonummer):
        """
        Sucht ein Bankkonto anhand der Kontonummer.
        Gibt ein Tupel (True, Bankkonto) bei Erfolg, sonst (False, None) zurück.
        """
        for bankkonto in self.kontos:
            if bankkonto.kontonummer == gesuchte_kontonummer:
                return (True,bankkonto)
        return (False,None)

    def bank_details(self):
        """
        Gibt eine Übersicht der Bankdetails wie Name, Standort, Anzahl Konten und Kunden zurück.
        """
        anzahl_kontos = len(self.kontos)
        anzahl_kunden = len(self.kunden)

        resultat = f'Wilkommen bei der {self.name}!\nWir sind eine Bank aus {self.land}, mit unser hauptstandort in {self.hauptstandort}.\nWir haben aktuell {anzahl_kontos} Kontos und {anzahl_kunden} Kunden!'
        return resultat

    def kunde_finden(self, vorname, nachname, adresse):
        """
        Sucht einen Kunden anhand von Vorname, Nachname und Adresse.
        Gibt ein Tupel (True, Kunde) bei Erfolg, sonst (False, None) zurück.
        """
        for kunde in self.kunden:
            if kunde.vorname == vorname and kunde.nachname == nachname and kunde.adresse == adresse:
                return (True,kunde)
        return (False,None)
        #Rueckgabewert ist ein Tupel mit (bool,kunde) oder (bool,None)
    
    def kunde_erstellen(self, vorname, nachname, adresse, telefonnummer, email, alter):
        """
        Erstellt einen neuen Kunden, falls dieser noch nicht existiert.
        Gibt True bei Erfolg, sonst False zurück.
        """
        neuer_kunde = Kunde(vorname, nachname, adresse, telefonnummer, email, alter)
        if not self.kunde_finden(vorname, nachname, adresse)[0]:
            #0 ist der bool wert aus den Tupel 
            #den wir von die Methode kunde_finden 
            # bekommen.
            self.kunden.append(neuer_kunde)
            print('Kunde erfolgreich erstellt.')
            return True
        else:
            print('Kunde existiert schon.')
            return False

    def kunde_loeschen(self, vorname, nachname, adresse):
        """
        Löscht einen Kunden anhand von Vorname, Nachname und Adresse.
        Gibt True bei Erfolg, sonst False zurück.
        """
        kunde_existiert_tupel = self.kunde_finden(vorname,nachname,adresse)
        if kunde_existiert_tupel[0]: 
            #0 ist der bool wert aus den Tupel 
            #den wir von die Methode kunde_finden 
            # bekommen.
            self.kunden.remove(kunde_existiert_tupel[1]) #1 Ist der Kunde selbst
            print('Kunde erfolgreich geloescht.')
            return True
        else:
            print('Kunde konnte nicht gefunden werden.')
            return False
        
    def bankkonto_loeschen(self, kontonummer):
        """
        Löscht ein Bankkonto anhand der Kontonummer.
        Gibt True bei Erfolg, sonst False zurück.
        """
        for bankkonto in self.kontos:
            #print(bankkonto.kontonummer)
            if bankkonto.kontonummer == kontonummer:
                self.kontos.remove(bankkonto)
                print('Bankkonto erfolgreich geloescht.')
                return True
        print("Dieser Bankkonto konnte nicht gefunden werden.")
        return False

    def bankkonto_erstellen(self,kunde):
        """
        Erstellt ein neues Bankkonto für einen Kunden mit einer einzigartigen Kontonummer.
        """
        tupel = self.freies_kontonummer_generieren()
        while not tupel[0]:
            tupel = self.freies_kontonummer_generieren()

        neuer_bankkonto = Bankkonto(kunde,tupel[1])
        self.kontos.append(neuer_bankkonto)

    #5-stelliges Kontonummer
    def freies_kontonummer_generieren(self):
        """
        Generiert eine freie, fünfstellige Kontonummer, die noch nicht vergeben ist.
        Gibt ein Tupel (True, Kontonummer) bei Erfolg, sonst (False, None) zurück.
        """
        neue_kontonummer = self.fuenf_stellige_kontonummer_erstellen()
        for konto in self.kontos:
            if neue_kontonummer == konto.kontonummer:
                return (False,None)   
        return (True,neue_kontonummer)

    def fuenf_stellige_kontonummer_erstellen(self):
        """
        Erstellt eine zufällige fünfstellige Kontonummer als String.
        """
        resultat = ''
        for i in range(0,5):
            resultat += str(randint(0,9))
        return resultat
    
    def alle_kontos_details(self):
        """
        Gibt die Details aller Bankkonten aus.
        """
        print('\n=================Konto Liste======================\n')
        for konto in self.kontos:
            konto.details()

    def alle_kunden_details(self):
        """
        Gibt die Details aller Kunden aus.
        """
        print('\n=================Kunde Liste======================\n')
        for kunde in self.kunden:
            kunde.detail_kunde()


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

class Kunde:
    def __init__(self, vorname, nachname, adresse, telefonnummer, email, alter):
        self.vorname = vorname
        self.nachname = nachname
        self.adresse = adresse
        self.telefonnumer = telefonnummer
        self.email = email
        self.alter = alter
    
    def detail_kunde(self,formatier_anzeige=True):
        if formatier_anzeige:
            print('==================================')
            print(f'Name: {self.vorname} {self.nachname}')
            print(f'Adresse: {self.adresse}. Email: {self.email}')
            print(f'Telefonnummer: {self.telefonnumer}')
            print('Alter:',self.alter)
            print('==================================')
        else:
            return f'{self.vorname} {self.nachname} {self.email}'