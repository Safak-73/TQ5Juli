class VehicleView:
    def display_vehicles(self, vehicles):
        print("=== 🚘 Fahrzeuge ===")
        for v in vehicles:
            # v = (VehicleID, Brand, Model, Year, DailyRate, Status)
            year_display = v[3] if v[3] is not None else "-"
            print(f"[{v[0]}] {v[1]} {v[2]} ({year_display}) | {v[4]} €/Tag | Status: {v[5]}")

    def get_vehicle_input(self):
        brand = input("👉 Marke: ")
        model = input("👉 Modell: ")
        year = input("👉 Baujahr (YYYY): ")
        try:
            year = int(year)
        except ValueError:
            year = None  # falls nichts eingegeben wird
        rate = float(input("👉 Preis pro Tag: "))
        return brand, model, year, rate

    def get_update_price_input(self):
        vid = int(input("👉 Fahrzeug-ID: "))
        rate = float(input("👉 Neuer Preis pro Tag: "))
        return vid, rate
