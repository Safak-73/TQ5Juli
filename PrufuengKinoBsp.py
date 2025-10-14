class Kinoticket:
    def __init__(self, filmname, preis, reihe, platz):
        self.filmname = filmname
        self.preis = preis
        self.reihe = reihe
        self.platz = platz

#Film: Dune 2, Reihe: 3, Platz: 5, Preis: 9.50 €
    def anzeigen(self):
        print(f'Film: {self.filmname}, Reihe: {self.reihe}, Platz: {self.platz}, Preis: {self.preis:.2f} €')

class Kinoverwaltung:
    def __init__(self):
        self.verkaufte_tickets = []

    def ticket_hinzufuegen(self, kinoticket):
        self.verkaufte_tickets.append(kinoticket)

    def gesamtumsatz(self):
        summe = 0
        for ticket in self.verkaufte_tickets:
            summe += ticket.preis
        return summe
    
if __name__ == '__main__':
    kino = Kinoverwaltung()

    kino.ticket_hinzufuegen(Kinoticket('Dune',9.5,3,5))
    kino.ticket_hinzufuegen(Kinoticket('Avatar',10,7,4))

    for tickets in kino.verkaufte_tickets:
        tickets.anzeigen()
