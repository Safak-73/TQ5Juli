class CustomerView:
    def get_rental_input(self):
        vid = int(input("👉 Fahrzeug-ID: "))
        start = input("👉 Startdatum (YYYY-MM-DD): ")
        end = input("👉 Enddatum (YYYY-MM-DD): ")
        return vid, start, end

    def display_rental_history(self, rentals):
        print("=== 📜 Meine Miet-Historie ===")
        if not rentals:
            print("⚠️ Keine Mietvorgänge gefunden.")
            return
        for r in rentals:
            print(f"#{r[0]} | {r[1]} {r[2]} | {r[3]} → {r[4]} | {r[5]} €")
