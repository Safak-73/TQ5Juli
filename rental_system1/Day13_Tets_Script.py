import time
import sys
from database.connection import get_connection
from controllers.user_controller import UserController
from controllers.vehicle_controller import VehicleController
from controllers.rental_controller import RentalController
from models.user_model import UserModel
import shutil

# -------------------------
# Farben für Status
# -------------------------
class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

def colored_status(status):
    if status == "Available":
        return f"{Color.GREEN}{status}{Color.RESET}"
    elif status == "Rented":
        return f"{Color.RED}{status}{Color.RESET}"
    elif status == "Maintenance":
        return f"{Color.YELLOW}{status}{Color.RESET}"
    return status

# -------------------------
# Helfer: Terminal-Zentrierung
# -------------------------
def print_centered(text):
    width = shutil.get_terminal_size().columns
    print(str(text).center(width))

def loading(duration=2, steps=10):
    """Kurzes Lade-Symbol animieren"""
    for i in range(steps):
        sys.stdout.write(f"\r{'Lädt' + '·' * (i % 4):^{shutil.get_terminal_size().columns}}")
        sys.stdout.flush()
        time.sleep(duration/steps)
    print("\r", end="")

# -------------------------
# Testdaten zurücksetzen
# -------------------------
def reset_test_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Alte Testdaten löschen
    cursor.execute("DELETE FROM User WHERE Username LIKE 'test_%'")
    cursor.execute("DELETE FROM Customer WHERE Name LIKE 'Testkunde%'")
    cursor.execute("DELETE FROM Vehicle WHERE Brand LIKE 'Testauto%'")
    cursor.execute("DELETE FROM Rental")
    cursor.execute("DELETE FROM Payment")

    # Neue Testdaten
    cursor.execute("INSERT INTO User (Username, Password, Role) VALUES ('test_customer','123','Customer')")
    cursor.execute("INSERT INTO User (Username, Password, Role) VALUES ('test_employee','123','Employee')")

    cursor.execute("""
        INSERT INTO Customer (UserID, Name, Phone)
        VALUES ((SELECT UserID FROM User WHERE Username='test_customer'),'Testkunde','123456')
    """)

    # Fahrzeuge
    cursor.execute("INSERT INTO Vehicle (Brand, Model, Year, DailyRate, Status) VALUES ('Testauto','Modell A',2023,50,'Available')")
    cursor.execute("INSERT INTO Vehicle (Brand, Model, Year, DailyRate, Status) VALUES ('Testauto','Modell B',2022,80,'Rented')")

    conn.commit()
    conn.close()
    print_centered("✅ Testdaten zurückgesetzt.\n")

# -------------------------
# Logo
# -------------------------
def print_logo():
    logo = r"""
  _____            _        _  _____           _                  __      __      __        ___         ___  
 |  __ \          | |      | |/ ____|         | |                 \ \    / /     /_ |      / _ \       / _ \ 
 | |__) |___ _ __ | |_ __ _| | (___  _   _ ___| |_ ___ _ __ ___    \ \  / /       | |     | | | |     | | | |
 |  _  // _ \ '_ \| __/ _` | |\___ \| | | / __| __/ _ \ '_ ` _ \    \ \/ /        | |     | | | |     | | | |
 | | \ \  __/ | | | || (_| | |____) | |_| \__ \ ||  __/ | | | | |    \  /     _   | |  _  | |_| |  _  | |_| |
 |_|  \_\___|_| |_|\__\__,_|_|_____/ \__, |___/\__\___|_| |_| |_|     \/     (_)  |_| (_)  \___/  (_)  \___/ 
                                      __/ |                                                                  
                                     |___/                                                                   
"""
    for line in logo.splitlines():
        print_centered(line)

# -------------------------
# Präsentation
# -------------------------
def run_presentation():
    print_logo()
    print_centered("🚀 Starte Vehicle Rental System Präsentation...\n")

    user_ctrl = UserController()
    vehicle_ctrl = VehicleController()
    rental_ctrl = RentalController()
    user_model = UserModel()

    input(print_centered("Drücke Enter zum Start der Präsentation..."))

    # --- Login Kunde ---
    print_centered("\n🔑 Login als Kunde")
    loading()
    user = user_model.get_user_by_credentials("test_customer","123")
    print_centered(f"✅ Angemeldet: {user['Username']} ({user['Role']})")
    input(print_centered("Drücke Enter, um verfügbare Fahrzeuge anzuzeigen..."))

    # Fahrzeuge ansehen (nur verfügbar)
    print_centered("\n🚘 Verfügbare Fahrzeuge für Kunde:")
    vehicles = vehicle_ctrl.model.get_available_vehicles()
    for v in vehicles:
        row = f"[{v[0]}] {v[1]} {v[2]} ({v[3]}) | {v[4]} €/Tag | Status: {colored_status(v[5])}"
        print_centered(row)
    input(print_centered("Drücke Enter, um ein Fahrzeug zu mieten..."))

    # Fahrzeug mieten
    print_centered("\n📑 Kunde mietet Fahrzeug")
    loading()
    if vehicles:
        vehicle_id = vehicles[0][0]
        ok, msg = rental_ctrl.rental_model.create_rental(
            user["UserID"], vehicle_id, "2025-10-01", "2025-10-03", vehicles[0][4]*2
        )
        print_centered(msg)
    input(print_centered("Drücke Enter, um Miet-Historie anzuzeigen..."))

    # Miet-Historie
    print_centered("\n📜 Miet-Historie Kunde:")
    rentals = rental_ctrl.rental_model.get_rentals_by_user(user["UserID"])
    for r in rentals:
        row = f"#{r[0]} | {r[1]} {r[2]} | {r[3]} → {r[4]} | {r[5]} €"
        print_centered(row)
    input(print_centered("Drücke Enter, um Fahrzeug zurückzugeben..."))

    # Fahrzeug zurückgeben
    print_centered("\n🔄 Fahrzeug zurückgeben")
    loading()
    rental_id = rentals[0][0]
    ok, msg, cost = rental_ctrl.rental_model.return_vehicle_and_get_cost(rental_id)
    print_centered(msg)
    rental_ctrl.payment_model.add_payment(rental_id, cost)
    input(print_centered("Drücke Enter, um als Employee einzuloggen..."))

    # --- Login Employee ---
    print_centered("\n🔑 Login als Employee")
    loading()
    emp = user_model.get_user_by_credentials("test_employee","123")
    print_centered(f"✅ Angemeldet: {emp['Username']} ({emp['Role']})")
    input(print_centered("Drücke Enter, um alle Fahrzeuge anzuzeigen..."))

    # Alle Fahrzeuge anzeigen inkl. Status
    print_centered("\n🚘 Alle Fahrzeuge für Employee:")
    vehicles = vehicle_ctrl.model.get_all_vehicles()
    for v in vehicles:
        row = f"[{v[0]}] {v[1]} {v[2]} ({v[3]}) | {v[4]} €/Tag | Status: {colored_status(v[5])}"
        print_centered(row)
    input(print_centered("Drücke Enter, um ein neues Fahrzeug hinzuzufügen..."))

    # Fahrzeug hinzufügen
    print_centered("\n➕ Fahrzeug hinzufügen")
    loading()
    vehicle_ctrl.model.add_vehicle("Testauto", "Modell C", 2024, 100
                                   )
    print_centered("✅ Fahrzeug 'Testauto Modell C' hinzugefügt")
    input(print_centered("Drücke Enter, um den Status eines Fahrzeugs zu ändern..."))

    # Fahrzeugstatus ändern (Maintenance)
    print_centered("\n🔧 Fahrzeugstatus ändern")
    loading()
    v_id = vehicles[0][0]
    vehicle_ctrl.model.update_status = lambda vid, status: vehicle_ctrl.model._update_status(vid, status)  # Patch-Methode
    # Wir fügen _update_status in VehicleModel ein
    from models.vehicle_model import VehicleModel
    def _update_status(self, vehicle_id, status):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Vehicle SET Status=? WHERE VehicleID=?", (status, vehicle_id))
        conn.commit()
        conn.close()
    VehicleModel._update_status = _update_status
    vehicle_ctrl.model._update_status(v_id, "Maintenance")
    print_centered(f"✅ Fahrzeug-ID {v_id} auf 'Maintenance' gesetzt")
    input(print_centered("Drücke Enter, um ein Fahrzeug zu entfernen..."))

    # Fahrzeug entfernen
    print_centered("\n❌ Fahrzeug entfernen")
    loading()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Vehicle WHERE Brand='Testauto' AND Model='Modell B'")
    conn.commit()
    conn.close()
    print_centered("✅ Fahrzeug 'Testauto Modell B' entfernt")

    input(print_centered("Drücke Enter, um final alle Fahrzeuge anzuzeigen..."))
    print_centered("\n🚘 Alle Fahrzeuge nach Änderungen:")
    vehicles = vehicle_ctrl.model.get_all_vehicles()
    for v in vehicles:
        row = f"[{v[0]}] {v[1]} {v[2]} ({v[3]}) | {v[4]} €/Tag | Status: {colored_status(v[5])}"
        print_centered(row)

    print_centered("\n🎉 Präsentation abgeschlossen!")

# -------------------------
# Start
# -------------------------
if __name__ == "__main__":
    reset_test_data()
    run_presentation()
