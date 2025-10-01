import sqlite3
import os
from datetime import datetime
from controllers.user_controller import UserController
from controllers.vehicle_controller import VehicleController
from controllers.rental_controller import RentalController
from models.user_model import UserModel

DB_PATH = os.path.join(os.path.dirname(__file__), "rental.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def debug_show_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("📂 Tabellen in DB:", cursor.fetchall())
    conn.close()

def debug_show_schema():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table'")
    for row in cursor.fetchall():
        print(row[0])
    conn.close()

def reset_test_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Vorher Testdaten löschen
    cursor.execute("DELETE FROM User WHERE Username LIKE 'test_%'")
    cursor.execute("DELETE FROM Customer WHERE Name LIKE 'Testkunde%'")
    cursor.execute("DELETE FROM Vehicle WHERE Brand LIKE 'Testauto%'")
    cursor.execute("DELETE FROM Rental")
    cursor.execute("DELETE FROM Payment")

    # User anlegen
    cursor.execute("INSERT INTO User (Username, Password, Role) VALUES ('test_customer', '123', 'Customer')")
    cursor.execute("INSERT INTO User (Username, Password, Role) VALUES ('test_employee', '123', 'Employee')")

    # Customer anlegen
    cursor.execute("""
        INSERT INTO Customer (Name, Phone, UserID)
        VALUES ('Testkunde', '123456',
                (SELECT UserID FROM User WHERE Username='test_customer'))
    """)

    # Test-Fahrzeug hinzufügen
    cursor.execute("INSERT INTO Vehicle (Brand, Model, DailyRate, Status) VALUES ('Testauto', 'Modell X', 50, 'Available')")

    conn.commit()
    conn.close()
    print("✅ Testdaten erfolgreich zurückgesetzt.")

def run_tests():
    print("\n🚀 Starte Tests...\n")

    user_controller = UserController()
    vehicle_controller = VehicleController()
    rental_controller = RentalController()

    # Login testen
    print("\n🔑 Test: Login als Kunde")
    user = UserModel().get_user_by_credentials("test_customer", "123")
    print("Login:", user)
    input("🔄 Weiter mit Enter ...")

    # Testauto suchen
    print("\n🚘 Test: Verfügbare Fahrzeuge")
    vehicles = vehicle_controller.model.get_available_vehicles()
    test_vehicle = [v for v in vehicles if v[1] == "Testauto"]
    if not test_vehicle:
        print("❌ Testauto nicht gefunden!")
        return
    vehicle_id = test_vehicle[0][0]
    print("Gefunden:", test_vehicle)
    input("🔄 Weiter mit Enter ...")

    # Mietzeitraum & Kosten berechnen
    start_date = "2025-10-01"
    end_date = "2025-10-03"
    days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
    if days <= 0:
        days = 1

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DailyRate FROM Vehicle WHERE VehicleID=?", (vehicle_id,))
    rate = cursor.fetchone()[0]
    conn.close()

    cost = days * rate
    print(f"\n📅 Mietzeitraum: {start_date} bis {end_date} ({days} Tage)")
    input("🔄 Weiter mit Enter ...")
    

    # Fahrzeug mieten
    print("\n📑 Test: Fahrzeug mieten")
    ok, msg = rental_controller.rental_model.create_rental(
        user["UserID"], vehicle_id, start_date, end_date, cost
    )
    print(msg)
    input("🔄 Weiter mit Enter ...")

    # Miet-Historie prüfen
    print("\n📜 Test: Miet-Historie Kunde")
    rentals = rental_controller.rental_model.get_rentals_by_user(user["UserID"])
    print(rentals)
    if not rentals: return
    rental_id = rentals[0][0]
    input("🔄 Weiter mit Enter ...")

    # Fahrzeug zurückgeben
    print("\n🔄 Test: Fahrzeug zurückgeben")
    ok, msg, cost = rental_controller.rental_model.return_vehicle_and_get_cost(rental_id)
    print(msg)
    input("🔄 Weiter mit Enter ...")

    # Zahlung hinzufügen
    print("\n💳 Test: Zahlung hinzufügen")
    rental_controller.payment_model.add_payment(rental_id, cost)
    print(f"✅ Zahlung über {cost} € gespeichert.")
    input("🔄 Weiter mit Enter ...")

    # Endkontrolle
    print("\n📜 Endkontrolle: Miet-Historie")
    rentals = rental_controller.rental_model.get_rentals_by_user(user["UserID"])
    for r in rentals: print(r)
    input("🔄 Weiter mit Enter ...")

    print("\n!!!🎉 Alle Tests abgeschlossen!!!")

if __name__ == "__main__":
    print(f"📌 Verwende Datenbank: {DB_PATH}")
    debug_show_tables()
    debug_show_schema()
    reset_test_data()
    run_tests()
