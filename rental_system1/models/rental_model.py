# models/rental_model.py
from database.connection import get_connection
import logging
from datetime import datetime

class RentalModel:
    """Datenzugriff für Mietverträge (Rental)."""

    def create_rental(self, user_id, vehicle_id, start_date, end_date, total_amount):
        """
        Erstelle einen Mietvertrag.
        Args:
            user_id: ID aus User-Tabelle (wir mappen intern auf CustomerID)
            vehicle_id: Fahrzeug-ID
            start_date, end_date: "YYYY-MM-DD"
            total_amount: berechneter Gesamtbetrag
        Returns:
            (ok: bool, message: str)
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # User -> CustomerID (Customer-Tabelle erwartet UserID FK)
            cursor.execute("SELECT CustomerID FROM Customer WHERE UserID=?", (user_id,))
            row = cursor.fetchone()
            if not row:
                conn.close()
                return False, "❌ Kein Customer-Datensatz für diesen User vorhanden."
            customer_id = row[0]

            # Fahrzeug prüfen
            cursor.execute("SELECT Status FROM Vehicle WHERE VehicleID=?", (vehicle_id,))
            v = cursor.fetchone()
            if not v:
                conn.close()
                return False, "❌ Fahrzeug nicht gefunden."
            status = v[0]
            if status != "Available":
                conn.close()
                return False, "❌ Fahrzeug ist nicht verfügbar."

            # Rental anlegen
            cursor.execute("""
                INSERT INTO Rental (VehicleID, CustomerID, StartDate, EndDate, TotalAmount, Status)
                VALUES (?, ?, ?, ?, ?, 'Active')
            """, (vehicle_id, customer_id, start_date, end_date, total_amount))

            # Fahrzeugstatus aktualisieren
            cursor.execute("UPDATE Vehicle SET Status='Rented' WHERE VehicleID=?", (vehicle_id,))

            conn.commit()
            conn.close()
            return True, "✅ Mietvertrag erfolgreich erstellt."
        except Exception as e:
            logging.error("Fehler create_rental: %s", e)
            return False, f"❌ Fehler beim Anlegen der Miete: {e}"

    def return_vehicle_and_get_cost(self, rental_id):
        """
        Rückgabe: berechne Kosten anhand Fahrzeug-Rate und Zeitraum,
        setze Rental-Status und Fahrzeugstatus zurück.
        Returns:
            (ok: bool, message: str, cost: float)
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT VehicleID, StartDate, EndDate, TotalAmount, Status
                FROM Rental WHERE RentalID=?
            """, (rental_id,))
            row = cursor.fetchone()
            if not row:
                conn.close()
                return False, "❌ Mietvertrag nicht gefunden.", 0.0

            vehicle_id, start, end, total_amount, status = row
            if status not in ("Active",):
                conn.close()
                return False, "⚠️ Mietvertrag ist nicht aktiv (bereits zurückgegeben?).", 0.0

            # Fahrzeug-Tagespreis holen
            cursor.execute("SELECT DailyRate FROM Vehicle WHERE VehicleID=?", (vehicle_id,))
            r = cursor.fetchone()
            if not r:
                conn.close()
                return False, "❌ Fahrzeug nicht gefunden.", 0.0
            daily_rate = r[0] or 0.0

            # Datumsberechnung
            start_dt = datetime.strptime(start, "%Y-%m-%d")
            end_dt = datetime.strptime(end, "%Y-%m-%d")
            days = (end_dt - start_dt).days
            if days <= 0:
                days = 1
            cost = days * daily_rate

            # Rental aktualisieren und Fahrzeug freigeben
            cursor.execute("""
                UPDATE Rental
                SET Status='Returned', TotalAmount=?
                WHERE RentalID=?
            """, (cost, rental_id))
            cursor.execute("UPDATE Vehicle SET Status='Available' WHERE VehicleID=?", (vehicle_id,))

            conn.commit()
            conn.close()
            return True, f"✅ Fahrzeug zurückgegeben. Gesamtkosten: {cost} €", cost
        except Exception as e:
            logging.error("Fehler return_vehicle_and_get_cost: %s", e)
            return False, f"❌ Fehler bei Rückgabe: {e}", 0.0

    def get_rentals_by_user(self, user_id):
        """
        Liefert alle Rentals für den eingeloggten User (UserID -> CustomerID).
        Returns: Liste von Rows: (RentalID, Brand, Model, StartDate, EndDate, TotalAmount)
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID FROM Customer WHERE UserID=?", (user_id,))
        r = cursor.fetchone()
        if not r:
            conn.close()
            return []
        customer_id = r[0]

        cursor.execute("""
            SELECT r.RentalID, v.Brand, v.Model, r.StartDate, r.EndDate, r.TotalAmount
            FROM Rental r
            JOIN Vehicle v ON r.VehicleID = v.VehicleID
            WHERE r.CustomerID=?
            ORDER BY r.StartDate DESC
        """, (customer_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_rentals_by_customerid(self, customer_id):
        """Für Mitarbeiter: Rentals nach CustomerID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.RentalID, v.Brand, v.Model, r.StartDate, r.EndDate, r.TotalAmount
            FROM Rental r
            JOIN Vehicle v ON r.VehicleID = v.VehicleID
            WHERE r.CustomerID=?
            ORDER BY r.StartDate DESC
        """, (customer_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows


