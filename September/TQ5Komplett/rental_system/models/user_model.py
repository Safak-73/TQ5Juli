import sqlite3
import logging

logging.basicConfig(filename='rental_error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Importiere die Verbindung und den Cursor aus der db_connection-Datei.
from database.db_connection import conn, cur

def get_user(user_id):
    """
    Ruft einen Benutzer anhand seiner ID ab.   
    Args:
        user_id (int): Die ID des Benutzers.
    """     
    try:
        cur.execute("SELECT * FROM User WHERE UserID = ?", (user_id,))
        return cur.fetchone()
    except sqlite3.Error as e:
        logging.error(f"Fehler beim Abrufen von Benutzer (ID: {user_id}): {e}")
        return None

def create_user(username, password, role):
    """
    Fügt einen neuen Benutzer in die Datenbank ein.
    
    Args:
        username (str): Der Benutzername.
        password (str): Das Passwort.
        role (str): Die Rolle ("Customer" oder "Employee").
    """
    try:
        # Führe den INSERT-Befehl aus
        cur.execute("INSERT INTO User (Username, Password, Role) VALUES (?, ?, ?)", (username, password, role))
        
        # Speichere die Änderungen in der Datenbank
        conn.commit()
        print(f"Benutzer '{username}' erfolgreich hinzugefügt.")
    except sqlite3.Error as e:
        logging.error(f"Fehler beim erstellen eines nutzers (ID: {username}): {e}")

def update_password(user_id, new_password):
    """
    Aktualisiert das Passwort eines Benutzers.
    
    Args:
        user_id (int): Die ID des Benutzers.
        new_password (str): Das neue Passwort.
    """
    try:
        # Führe den UPDATE-Befehl aus
        cur.execute("UPDATE User SET Password = ? WHERE UserID = ?", (new_password, user_id))
        
        # Speichere die Änderungen in der Datenbank
        conn.commit()
        print(f"Passwort für Benutzer '{user_id}' erfolgreich aktualisiert.")
    except sqlite3.Error as e:
        logging.error(f"Fehler beim Password ändern (ID: {user_id}): {e}")

def get_login(username, password):
    """
    Sucht einen Benutzer anhand des Benutzernamens und Passworts.
    """
    try:
        cur.execute("SELECT * FROM User WHERE Username = ? AND Password = ?", (username, password))
        return cur.fetchone()
    except sqlite3.Error as e:
        logging.error(f"Datenbankfehler beim Login von Benutzer '{username}': {e}")
        return None
