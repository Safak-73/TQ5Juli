from controllers.vehicle_controller import show_available_vehicles
 
def show_customer_menu():
    while True:
        print("\n=== Kundenmenü ===")
        print("1. Fahrzeug suchen")
        print("2. Mietverträge anzeigen")
        print("3. Zurück zum Hauptmenü")
 
        choice = input("Auswahl: ")
        if choice == "1":
            show_available_vehicles()  # ← Hier wird die Funktion aufgerufen
        elif choice == "2":
            print("🔧 Mietverträge anzeigen (noch nicht implementiert)")
        elif choice == "3":
            break
        else:
            print("❌ Ungültige Eingabe.")