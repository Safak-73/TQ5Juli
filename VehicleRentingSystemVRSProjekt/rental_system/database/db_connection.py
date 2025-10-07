# file name:    db_connection.py
# file path:    rental_system/database/db_connection.pyimport sqlite3


import os
import sqlite3
import logging


DB_FILE = "rental.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
   
    conn.row_factory = sqlite3.Row
    # Foreign Keys aktivieren
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

def init_db():
    with get_connection() as conn:
        cur = conn.cursor()
        # User
        cur.execute("""
        CREATE TABLE IF NOT EXISTS User (
            UserID INTEGER PRIMARY KEY,
            Username TEXT UNIQUE NOT NULL,
            PasswordHash TEXT NOT NULL,
            Salt TEXT NOT NULL,
            Role TEXT NOT NULL CHECK(Role IN ('Employee','Customer'))
        );
        """)
        # Customer
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerID INTEGER PRIMARY KEY,
            UserID INTEGER UNIQUE,
            Name TEXT NOT NULL,
            Email TEXT UNIQUE NOT NULL,
            Phone TEXT,
            FOREIGN KEY(UserID) REFERENCES User(UserID) ON DELETE CASCADE
        );
        """)
        # Vehicle
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Vehicle (
            VehicleID INTEGER PRIMARY KEY,
            Brand TEXT NOT NULL,
            Model TEXT NOT NULL,
            Year INTEGER NOT NULL CHECK(Year >= 1900),
            DailyRate REAL NOT NULL CHECK(DailyRate >= 0),
            Status TEXT NOT NULL CHECK(Status IN ('Available','Rented','Maintenance')) DEFAULT 'Available'
        );
        """)
        # Rental
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Rental (
            RentalID INTEGER PRIMARY KEY,
            VehicleID INTEGER NOT NULL,
            CustomerID INTEGER NOT NULL,
            StartDate TEXT NOT NULL, -- ISO-8601 'YYYY-MM-DD'
            EndDate TEXT NOT NULL,
            TotalAmount REAL NOT NULL CHECK(TotalAmount >= 0),
            Status TEXT NOT NULL CHECK(Status IN ('Active','Completed','Cancelled')) DEFAULT 'Active',
            FOREIGN KEY(VehicleID) REFERENCES Vehicle(VehicleID),
            FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID)
        );
        """)
        # Payment
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Payment (
            PaymentID INTEGER PRIMARY KEY,
            RentalID INTEGER NOT NULL,
            Amount REAL NOT NULL CHECK(Amount >= 0),
            PaymentDate TEXT NOT NULL, -- ISO-8601 'YYYY-MM-DD'
            FOREIGN KEY(RentalID) REFERENCES Rental(RentalID) ON DELETE CASCADE
        );
        """)

if __name__ == "__main__":
    init_logging()
    try:
        init_db()
        print("rental.db wurde erfolgreich erstellt.")
    except Exception as e:
        print(f"Fehler beim Erstellen der Datenbank: {e}")