# controllers/user_controller.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importiere alle notwendigen Funktionen
from models.user_model import get_login
from models.vehicle_model import get_all_vehicles, add_vehicle, update_vehicle_status, get_available_vehicles, get_vehicle_status
from models.rental_model import get_active_rentals, create_rental, return_vehicle, get_user_rental_history, get_vehicle_id_from_rental, get_rental_status
from views.customer_view import show_customer_menu
from views.employee_view import show_employee_menu

def handle_user_management(user_role, user_id):
    """
    Steuert die Menü-Logik basierend auf der Benutzerrolle.
    """
    if user_role == "Employee":
        while True:
            choice = show_employee_menu()

            if choice == '1':
                print("\nAlle Fahrzeuge:")
                vehicles = get_all_vehicles()
                for vehicle in vehicles:
                    print(f"ID: {vehicle[0]}, Marke: {vehicle[1]}, Modell: {vehicle[2]}, Baujahr: {vehicle[3]}, Ratenhöhe: {vehicle[4]}, Status: {vehicle[5]}")
            
            elif choice == '2':
                brand = input("Marke: ")
                model = input("Modell: ")
                year = int(input("Baujahr: "))
                daily_rate = float(input("Ratenhöhe: "))
                add_vehicle(brand, model, year, daily_rate)

            elif choice == '3':
                vehicle_id = int(input("Fahrzeug-ID: "))
                new_status = input("Neuer Status (Available, Rented, Maintenance): ")
                update_vehicle_status(vehicle_id, new_status)

            elif choice == '4':
                print("\nAlle aktiven Vermietungen:")
                rentals = get_active_rentals()
                for rental in rentals:
                    print(f"Vermietungs-ID: {rental[0]}, Fahrzeug-ID: {rental[1]}, Kunden-ID: {rental[2]}")
            
            elif choice == '5':
                print("Abmeldung...")
                break
            
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl von 1 bis 5.")
                
    elif user_role == "Customer":
        while True:
            choice = show_customer_menu()
            
            if choice == '1':
                print("\nVerfügbare Fahrzeuge:")
                vehicles = get_available_vehicles()
                for vehicle in vehicles:
                    print(f"ID: {vehicle[0]}, Marke: {vehicle[1]}, Modell: {vehicle[2]}")

            elif choice == '2':
                vehicle_id = int(input("Fahrzeug-ID: "))
                status = get_vehicle_status(vehicle_id)

                if status == 'Available':
                    create_rental(user_id, vehicle_id)
                    update_vehicle_status(vehicle_id, 'Rented')
                else:
                    print(f"\nFehler: Fahrzeug mit ID {vehicle_id} ist nicht verfügbar. Aktueller Status: {status}")

            elif choice == '3':
                print("\nFahrzeug zurückgeben:")
                rental_id = int(input("Vermietungs-ID: "))
                
                # NEUE LOGIK: Zuerst den Status prüfen
                rental_status = get_rental_status(rental_id)
                
                if rental_status == 'Completed':
                    print("Dieses Fahrzeug wurde bereits zurückgegeben.")
                elif rental_status == 'Active':
                    # Holen der Fahrzeug-ID aus der Datenbank und Überprüfung des Benutzers
                    vehicle_id_to_return = get_vehicle_id_from_rental(rental_id, user_id)
                    
                    if vehicle_id_to_return:
                        return_vehicle(rental_id)
                        update_vehicle_status(vehicle_id_to_return, 'Available')
                    else:
                        print("Fehler: Vermietungs-ID nicht gefunden oder gehört nicht zu Ihrem Konto.")
                else:
                    print("Fehler: Ungültige Vermietungs-ID.")

            
            elif choice == '4':
                print("\nIhre Miet-Historie:")
                history = get_user_rental_history(user_id)
                for rental in history:
                    print(f"Vermietungs-ID: {rental[0]}, Fahrzeug-ID: {rental[1]}, Startdatum: {rental[3]}, Enddatum: {rental[4]}")

            elif choice == '5':
                print("Abmeldung...")
                break
                
            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl von 1 bis 5.")


def handle_login():
    """Steuert den Anmeldeprozess und leitet zum Menü weiter."""
    print("===== LOGIN =====")
    username = input("Benutzername: ")
    password = input("Passwort: ")

    user = get_login(username, password)
    
    if user:
        print(f"\nLogin erfolgreich! Willkommen, {user[1]}!")
        handle_user_management(user[3], user[0])
    else:
        print("\nLogin fehlgeschlagen. Ungültige Anmeldedaten.")

if __name__ == "__main__":
    handle_login()