import sqlite3


class RentalModel:
    def __init__(self, db_path="rental.db"):
        self.db_path = db_path

    def create_rental(self, user_id, vehicle_id, start_date, end_date, cost):
        """Neuen Mietvertrag anlegen (nur wenn Fahrzeug Available ist)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # prüfen ob Fahrzeug verfügbar
        cursor.execute("SELECT Status FROM Vehicle WHERE VehicleID=?", (vehicle_id,))
        result = cursor.fetchone()
        if not result or result[0] != "Available":
            conn.close()
            return False, "❌ Fahrzeug nicht verfügbar!"

        # neuen Rental-Eintrag erstellen
        cursor.execute("""
            INSERT INTO Rental (UserID, VehicleID, StartDate, EndDate, TotalCost)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, vehicle_id, start_date, end_date, cost))

        # Fahrzeugstatus auf "Rented" setzen
        cursor.execute("UPDATE Vehicle SET Status='Rented' WHERE VehicleID=?", (vehicle_id,))
        conn.commit()
        conn.close()

        return True, "✅ Fahrzeug erfolgreich gemietet!"

    def return_vehicle(self, rental_id, kilometers, daily_rate):
        """Fahrzeug zurückgeben + Kosten berechnen."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Rental abrufen
        cursor.execute("""
            SELECT VehicleID, StartDate, EndDate FROM Rental WHERE RentalID=?
        """, (rental_id,))
        rental = cursor.fetchone()

        if not rental:
            conn.close()
            return False, "❌ Mietvertrag nicht gefunden!"

        vehicle_id, start_date, end_date = rental

        # Kosten neu berechnen (z. B. Tage × daily_rate, vereinfacht)
        from datetime import datetime
        d1 = datetime.strptime(start_date, "%Y-%m-%d")
        d2 = datetime.strptime(end_date, "%Y-%m-%d")
        days = (d2 - d1).days or 1
        total_cost = days * daily_rate

        # Rental updaten
        cursor.execute("""
            UPDATE Rental
            SET TotalCost=?, ReturnDate=date('now')
            WHERE RentalID=?
        """, (total_cost, rental_id))

        # Fahrzeug wieder freigeben
        cursor.execute("UPDATE Vehicle SET Status='Available' WHERE VehicleID=?", (vehicle_id,))
        conn.commit()
        conn.close()

        return True, f"✅ Rückgabe erfolgreich! Gesamtkosten: {total_cost} €"
