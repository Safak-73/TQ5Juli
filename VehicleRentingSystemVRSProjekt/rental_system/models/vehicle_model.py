from database.db_connection import get_connection
import sqlite3
 
class VehicleModel:
    @staticmethod
    def get_available_vehicles():
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Vehicle WHERE Status = 'Available'")
        vehicles = cur.fetchall()
        conn.close()
        return vehicles