# models/rental_model.py
import sqlite3
import datetime

# Importiere die Verbindung und den Cursor aus der db_connection-Datei.
from database.db_connection import conn, cur

def get_vehicle_id_from_rental(rental_id, customer_id):
    """Gibt die Fahrzeug-ID basierend auf der Vermietungs-ID zurück."""
    try:
        cur.execute("SELECT VehicleID FROM Rental WHERE RentalID = ? AND CustomerID = ?", (rental_id, customer_id))
        result = cur.fetchone()
        if result:
            return result[0]
        return None
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return None

def create_rental(customer_id, vehicle_id):
    """
    Erstellt eine neue Vermietung in der Datenbank mit dem Status 'Active'.
    """
    try:
        rent_date = datetime.date.today().isoformat()
        cur.execute("INSERT INTO Rental (CustomerID, VehicleID, StartDate, Status) VALUES (?, ?, ?, ?)", (customer_id, vehicle_id, rent_date, 'Active'))
        conn.commit()
        print(f"Fahrzeug {vehicle_id} erfolgreich an Benutzer {customer_id} vermietet.")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")

def return_vehicle(rental_id):
    """
    Aktualisiert den Status einer Vermietung auf 'Completed'.
    """
    try:
        return_date = datetime.date.today().isoformat()
        cur.execute("UPDATE Rental SET EndDate = ?, Status = 'Completed' WHERE RentalID = ?", (return_date, rental_id))
        conn.commit()
        print(f"Vermietung {rental_id} erfolgreich abgeschlossen.")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")

def get_active_rentals():
    """
    Gibt alle aktiven Vermietungen zurück (basierend auf dem Status).
    """
    try:
        cur.execute("SELECT * FROM Rental WHERE Status = 'Active'")
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []

def get_user_rental_history(customer_id):
    """
    Gibt die gesamte Vermietungshistorie eines Benutzers zurück.
    """
    try:
        cur.execute("SELECT * FROM Rental WHERE CustomerID = ?", (customer_id,))
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []
    
def get_rental_status(rental_id):
    """Gibt den Status eines Mietvertrags zurück."""
    try:
        cur.execute("SELECT Status FROM Rental WHERE RentalID = ?", (rental_id,))
        result = cur.fetchone()
        if result:
            return result[0]
        return None
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return None

def get_rental_dates(rental_id):
    """
    Gibt das Start- und Enddatum eines Mietvertrags zurück.
    """
    try:
        cur.execute("SELECT StartDate, EndDate FROM Rental WHERE RentalID = ?", (rental_id,))
        result = cur.fetchone()
        if result:
            return result
        return None
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return None