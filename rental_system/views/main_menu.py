class MainMenuView:
    def get_login_input(self):
        print("\n🔑 Bitte logge dich ein:")
        username = input("👤 Benutzername: ")
        password = input("🔒 Passwort: ")
        return username, password

    def show_login_success(self, user):
        print(f"\n✅ Willkommen {user['Username']}! Rolle: {user['Role']}")

    def show_login_failure(self):
        print("❌ Login fehlgeschlagen. Bitte überprüfe Benutzername oder Passwort.")

    def customer_menu(self):
        print("\n╔═══════════════════════╗")
        print("║       📋 Kundenmenü   ║")
        print("╚═══════════════════════╝")
        print("1️⃣  Fahrzeug mieten")
        print("2️⃣  Bestand ansehen")
        print("3️⃣  Exit")
        return input("👉 Deine Auswahl: ")

    def employee_menu(self):
        print("\n╔════════════════════════════╗")
        print("║     🛠️  Mitarbeitermenü     ║")
        print("╚════════════════════════════╝")
        print("1️⃣  Fahrzeug mieten")
        print("2️⃣  Bestand ansehen")
        print("3️⃣  Fahrzeug hinzufügen")
        print("4️⃣  Preis bearbeiten")
        print("5️⃣  Exit")
        return input("👉 Deine Auswahl: ")
