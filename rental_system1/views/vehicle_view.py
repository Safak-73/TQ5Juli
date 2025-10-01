class VehicleView:
    def display_vehicles(self, vehicles):
        print("=== 🚘 Fahrzeuge ===")
        if not vehicles:
            print("⚠️ Keine Fahrzeuge gefunden.")
            return
        for v in vehicles:
            # v = (VehicleID, Brand, Model, Year, DailyRate, Status)
            year = v[3] if v[3] else "unbekannt"
            print(f"[{v[0]}] {v[1]} {v[2]} ({year}) | {v[4]} €/Tag | Status: {v[5]}")

    def get_vehicle_input(self):
        brand = input("👉 Marke: ")
        model = input("👉 Modell: ")
        year = int(input("👉 Baujahr: "))
        rate = float(input("👉 Preis pro Tag: "))
        return brand, model, year, rate

    def get_update_price_input(self):
        vid = int(input("👉 Fahrzeug-ID: "))
        rate = float(input("👉 Neuer Preis pro Tag: "))
        return vid, rate
