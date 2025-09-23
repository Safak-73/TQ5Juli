from models.vehicle_model import VehicleModel
from views.main_menu import show_vehicle_list
 
def show_available_vehicles():
    vehicles = VehicleModel.get_available_vehicles()
    show_vehicle_list(vehicles)