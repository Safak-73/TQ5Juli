class MainMenu:
    def __init__(self):
        self.logo = r"""
   ____            _       _               _      
  |  _ \ __ _ _ __(_) __ _| |__   ___ _ __(_) ___ 
  | |_) / _` | '__| |/ _` | '_ \ / _ \ '__| |/ __|
  |  __/ (_| | |  | | (_| | | | |  __/ |  | | (__ 
  |_|   \__,_|_|  |_|\__, |_| |_|\___|_|  |_|\___|
                     |___/                        
        """

    def show_customer_menu(self):
        print(self.logo)
        print("=== 🚗 Hauptmenü (Kunde) ===")
        print("1. Verfügbare Fahrzeuge ansehen")
        print("2. Fahrzeug mieten")
        print("3. Fahrzeug zurückgeben")
        print("4. Meine Miet-Historie")
        print("0. Exit")
        return input("👉 Auswahl: ")

    def show_employee_menu(self):
        print(self.logo)
        print("=== 🛠️ Hauptmenü (Mitarbeiter) ===")
        print("1. Alle Fahrzeuge anzeigen")
        print("2. Fahrzeug hinzufügen")
        print("3. Preis ändern")
        print("4. Kundenhistorie anzeigen")
        print("0. Exit")
        return input("👉 Auswahl: ")
