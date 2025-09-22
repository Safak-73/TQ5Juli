from models.rental_model import RentalModel


class RentalController:
    def __init__(self):
        self.model = RentalModel()

    def rent_vehicle(self, user_id):
        """Fahrzeug mieten – Eingaben abfragen und Rental speichern."""
        vehicle_id = int(input("👉 Fahrzeug-ID eingeben: "))
        start_date = input("📅 Startdatum (YYYY-MM-DD): ")
        end_date = input("📅 Enddatum (YYYY-MM-DD): ")

        # Mietdauer berechnen (vereinfacht: 1 Tag = 50€, später dynamisch mit Vehicle-Tarif)
        from datetime import datetime
        d1 = datetime.strptime(start_date, "%Y-%m-%d")
        d2 = datetime.strptime(end_date, "%Y-%m-%d")
        days = (d2 - d1).days or 1
        daily_rate = 50
        cost = days * daily_rate

        ok, msg = self.model.create_rental(user_id, vehicle_id, start_date, end_date, cost)
        print(msg)

    def return_vehicle(self):
        """Fahrzeug zurückgeben."""
        rental_id = int(input("👉 Rental-ID eingeben: "))
        kilometers = int(input("🚗 Gefahrene Kilometer: "))
        daily_rate = 50  # Platzhalter (später dynamisch)

        ok, msg = self.model.return_vehicle(rental_id, kilometers, daily_rate)
        print(msg)
