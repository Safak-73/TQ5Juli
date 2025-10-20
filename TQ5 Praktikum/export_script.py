import os
import sqlite3
import sys

# === 1. Name der Datenbank-Datei ===
DB_NAME = "datenbank.db"

# === 2. Absoluten Pfad zur Datenbank berechnen ===
# __file__ = Pfad zu dieser .py-Datei
# os.path.dirname(__file__) = Ordner, in dem sie liegt
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, DB_NAME)

# === 3. Prüfen, ob Datei existiert ===
if not os.path.exists(db_path):
    print("❌ Fehler: Die Datenbankdatei wurde nicht gefunden!")
    print(f"Erwarteter Speicherort: {db_path}")
    print("\nBitte überprüfe, ob:")
    print("  • die Datei existiert, und")
    print("  • dein Script im richtigen Ordner liegt.")
    sys.exit(1)  # Script mit Fehler beenden

# === 4. Verbindung herstellen ===
print(f"✅ Datenbank gefunden unter: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# === 5. Test: Tabellen anzeigen ===
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
if tables:
    print("📋 Tabellen in der Datenbank:")
    for t in tables:
        print("  -", t[0])
else:
    print("⚠️ Keine Tabellen gefunden (leere Datenbank?)")

conn.close()
print("✅ Verbindung erfolgreich getestet.")