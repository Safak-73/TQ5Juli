import sqlite3
import os

# Absoluter Pfad zur rental.db
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "rental.db")

def get_connection():
    """Gibt eine neue Verbindung zur SQLite-Datenbank zurück."""
    return sqlite3.connect(DB_PATH)
