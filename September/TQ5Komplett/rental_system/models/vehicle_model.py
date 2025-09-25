# models/vehicle_model.py
import sqlite3
import logging

logging.basicConfig(filename='rental_error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Importiere die Verbindung und den Cursor aus der db_connection-Datei.
from database.db_connection import conn, cur

def get_all_vehicles():
    """
    Gibt alle Fahrzeuge aus der Datenbank zurück.
    """
    try:
        cur.execute("SELECT * FROM Vehicle")
        return cur.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Fehler beim Abrufen aller Fahrzeuge: {e}")
        return []

def add_vehicle(brand, model, year, daily_rate, status='Available'):
    """Fügt ein neues Fahrzeug in die Datenbank ein."""
    try:
        cur.execute("INSERT INTO Vehicle (Brand, Model, Year, DailyRate, Status) VALUES (?, ?, ?, ?, ?)", (brand, model, year, daily_rate, status))
        conn.commit()
        print(f"Fahrzeug {brand} {model} erfolgreich hinzugefügt.")
    except sqlite3.Error as e:
        logging.error(f"Fehler beim eintragen von Fahrzeug: {e}")

def get_available_vehicles():
    """
    Gibt alle verfügbaren Fahrzeuge zurück.
    """
    try:
        cur.execute("SELECT * FROM Vehicle WHERE Status = 'Available'")
        return cur.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Fehler beim zeigen aller Fahrzeuge: {e}")
        return []

def get_vehicle_status(vehicle_id):
    """
    Gibt den aktuellen Status eines Fahrzeugs zurück.
    """
    try:
        cur.execute("SELECT Status FROM Vehicle WHERE VehicleID = ?", (vehicle_id,))
        result = cur.fetchone()
        if result:
            return result[0]
        return None
    except sqlite3.Error as e:
        logging.error(f"Fehler beim Abrufen vom Fahrzeug status: {vehicle_id} - {e}")
        return None
        
def update_vehicle_status(vehicle_id, new_status):
    """
    Aktualisiert den Status eines Fahrzeugs in der Datenbank.
    """
    try:
        cur.execute("UPDATE Vehicle SET Status = ? WHERE VehicleID = ?", (new_status, vehicle_id))
        conn.commit()
        print(f"Status von Fahrzeug {vehicle_id} erfolgreich auf '{new_status}' aktualisiert.")
    except sqlite3.Error as e:
        logging.error(f"Fehler beim Updaten vom Fahrzeug Status: {vehicle_id} - {e}")

def get_daily_rate(vehicle_id):
    """
    Gibt die Tagesrate (DailyRate) eines Fahrzeugs zurück.
    """
    try:
        cur.execute("SELECT DailyRate FROM Vehicle WHERE VehicleID = ?", (vehicle_id,))
        result = cur.fetchone()
        if result:
            return result[0]
        return None
    except sqlite3.Error as e:
        logging.error(f"Fehler beim Abrufen von Tagesrate: {vehicle_id} - {e}")
        return None