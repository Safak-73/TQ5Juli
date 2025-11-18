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