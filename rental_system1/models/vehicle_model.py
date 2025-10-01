from database.connection import get_connection 

class VehicleModel:
    def get_all_vehicles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VehicleID, Brand, Model, Year, DailyRate, Status FROM Vehicle")
        vehicles = cursor.fetchall()
        conn.close()
        return vehicles

    def get_available_vehicles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT VehicleID, Brand, Model, Year, DailyRate, Status FROM Vehicle WHERE Status='Available'"
        )
        vehicles = cursor.fetchall()
        conn.close()
        return vehicles

    def add_vehicle(self, brand, model, year, daily_rate):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Vehicle (Brand, Model, Year, DailyRate, Status) VALUES (?, ?, ?, ?, 'Available')",
            (brand, model, year, daily_rate),
        )
        conn.commit()
        conn.close()

    def update_price(self, vehicle_id, new_rate):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Vehicle SET DailyRate=? WHERE VehicleID=?", (new_rate, vehicle_id))
        conn.commit()
        conn.close()

