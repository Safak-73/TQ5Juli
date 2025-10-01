# controllers/rental_controller.py
from models.rental_model import RentalModel
from models.payment_model import PaymentModel
from views.customer_view import CustomerView
from views.employee_view import EmployeeView
from database.connection import get_connection
from datetime import datetime

class RentalController:
    def __init__(self):
        self.rental_model = RentalModel()
        self.payment_model = PaymentModel()
        self.cview = CustomerView()
        self.eview = EmployeeView()

    def rent_vehicle(self, user_id):
        """Interaktive Miete (fragt View ab, berechnet Kosten, legt Rental an)."""
        vehicle_id, start_date, end_date = self.cview.get_rental_input()

        # Tagesrate aus DB holen (zentrale Connection)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DailyRate FROM Vehicle WHERE VehicleID=?", (vehicle_id,))
        r = cursor.fetchone()
        conn.close()
        if not r:
            print("❌ Fahrzeug nicht gefunden.")
            return
        daily_rate = r[0] or 0.0

        # Tage berechnen
        try:
            days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
            if days <= 0:
                days = 1
        except Exception:
            print("❌ Ungültiges Datum. Bitte im Format YYYY-MM-DD eingeben.")
            return

        cost = days * daily_rate

        ok, msg = self.rental_model.create_rental(user_id, vehicle_id, start_date, end_date, cost)
        print(msg)

    def return_vehicle(self):
        """Interaktive Rückgabe: berechnet Kosten, speichert Zahlung."""
        try:
            rental_id = int(input("👉 Rental-ID eingeben: "))
        except ValueError:
            print("❌ Ungültige Rental-ID.")
            return

        ok, msg, cost = self.rental_model.return_vehicle_and_get_cost(rental_id)
        print(msg)
        if ok:
            # Zahlung speichern
            self.payment_model.record_payment(rental_id, cost)
            print("✅ Zahlung erfasst.")

    def show_customer_history(self, user_id):
        """Zeige Miet-Historie für eingeloggten User."""
        rentals = self.rental_model.get_rentals_by_user(user_id)
        self.cview.display_rental_history(rentals)

    def show_customer_history_by_customerid(self):
        """Mitarbeiter-Funktion: History für beliebigen CustomerID anzeigen."""
        cid = self.eview.get_customer_id_for_history()
        rentals = self.rental_model.get_rentals_by_customerid(cid)
        self.cview.display_rental_history(rentals)
