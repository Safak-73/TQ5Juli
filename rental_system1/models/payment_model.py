from database.connection import get_connection
import datetime

class PaymentModel:
    def record_payment(self, rental_id, amount):
        """Speichert eine Zahlung in der Datenbank."""
        conn = get_connection()
        cursor = conn.cursor()
        payment_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO Payment (RentalID, Amount, PaymentDate)
            VALUES (?, ?, ?)
        """, (rental_id, amount, payment_date))
        conn.commit()
        conn.close()
        return True

    def add_payment(self, rental_id, amount):
        """Alias für record_payment, für Kompatibilität mit anderen Modulen."""
        return self.record_payment(rental_id, amount)

    def get_payments_for_rental(self, rental_id):
        """Alle Zahlungen zu einem Mietvertrag abrufen."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT PaymentID, Amount, PaymentDate
            FROM Payment
            WHERE RentalID=?
        """, (rental_id,))
        payments = cursor.fetchall()
        conn.close()
        return payments