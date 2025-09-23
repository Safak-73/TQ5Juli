from database.db_connection import init_db, init_logging, get_connection
from models.user_model import UserModel, hash_password
from controllers.user_controller import login
import sqlite3
 
def main():
    init_logging()
    init_db()
 
    # Testdaten einfügen (nur einmal ausführen!)
    try:
        # Prüfen, ob Benutzer 'admin' bereits existiert
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM User WHERE Username = ?", ("admin",))
            if not cur.fetchone():
                username = "admin"
                password = "geheim"
                salt = "zufälliger_salt"
                password_hash = hash_password(password, salt)
 
                cur.execute("""
                    INSERT INTO User (Username, PasswordHash, Salt, Role)
                    VALUES (?, ?, ?, ?)
                """, (username, password_hash, salt, "Employee"))
                conn.commit()
                print("Testbenutzer 'admin' wurde eingefügt.")
            else:
                print("ℹTestbenutzer 'admin' existiert bereits.")
 
        # Prüfen, ob Benutzer 'kunde1' bereits existiert
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM User WHERE Username = ?", ("kunde1",))
            if not cur.fetchone():
                UserModel.save_user("kunde1", "1234", "Customer")
                print("Testbenutzer 'kunde1' wurde eingefügt.")
            else:
                print("ℹTestbenutzer 'kunde1' existiert bereits.")
 
        # Prüfen, ob Fahrzeuge bereits existieren
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM Vehicle")
            count = cur.fetchone()[0]
            if count == 0:
                vehicles = [
                    ("BMW", "X3", 2022, 59.99, "Available"),
                    ("Audi", "A4", 2021, 49.99, "Available"),
                    ("VW", "Golf", 2020, 39.99, "Available")
                ]
                for brand, model, year, rate, status in vehicles:
                    cur.execute("""
                        INSERT INTO Vehicle (Brand, Model, Year, DailyRate, Status)
                        VALUES (?, ?, ?, ?, ?)
                    """, (brand, model, year, rate, status))
 
                conn.commit()
                print("✅ Testfahrzeuge wurden eingefügt.")
            else:
                print("ℹ️ Fahrzeuge sind bereits vorhanden.")
 
    except Exception as e:
        print(f"❌ Fehler beim Einfügen der Testdaten: {e}")
 
    # Login starten
    login()
 
if __name__ == "__main__":
    main()