def show_login_screen():
    print("=== Fahrzeugvermietung Login ===")
    username = input("Benutzername: ")
    password = input("Passwort: ")
    return username, password
 
def show_login_failed():
    print("Login fehlgeschlagen. Bitte überprüfe deine Eingaben.")
 
def show_welcome(role):
    print(f"Login erfolgreich. Rolle: {role}")
 
def show_vehicle_list(vehicles):
    print("\n🚗 Verfügbare Fahrzeuge:")
    if not vehicles:
        print("⚠️ Keine Fahrzeuge verfügbar.")
    for v in vehicles:
        print(f"- {v['Brand']} {v['Model']} ({v['Year']}) – {v['DailyRate']} €/Tag [ID: {v['VehicleID']}]")