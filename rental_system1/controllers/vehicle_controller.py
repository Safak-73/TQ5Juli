from models.vehicle_model import VehicleModel
from views.vehicle_view import VehicleView

class VehicleController:
    def __init__(self):
        self.model = VehicleModel()
        self.view = VehicleView()

    def show_all_vehicles(self):
        """Alle Fahrzeuge anzeigen, inkl. Status"""
        vehicles = self.model.get_all_vehicles()
        self.view.display_vehicles(vehicles)

    def show_available_vehicles(self):
        """Nur verfügbare Fahrzeuge anzeigen"""
        vehicles = self.model.get_available_vehicles()
        self.view.display_vehicles(vehicles)

    def add_vehicle(self):
        brand, model, year, rate = self.view.get_vehicle_input()
        self.model.add_vehicle(brand, model, year, rate)
        print("✅ Fahrzeug hinzugefügt!")

    def update_price(self):
        vid, new_rate = self.view.get_update_price_input()
        self.model.update_price(vid, new_rate)
        print("✅ Preis aktualisiert!")
