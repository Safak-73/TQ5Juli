from controllers.user_controller import UserController
from controllers.vehicle_controller import VehicleController
from controllers.rental_controller import RentalController
from views.main_menu import MainMenu


def main():
    user_controller = UserController()
    vehicle_controller = VehicleController()
    rental_controller = RentalController()
    menu = MainMenu()

    # Login
    user = user_controller.login()
    if not user:
        print("❌ Login fehlgeschlagen!")
        return

    # Rollenbasiertes Menü
    while True:
        if user["Role"] == "Customer":
            choice = menu.show_customer_menu()
            if choice == "1":
                vehicle_controller.show_available_vehicles()
            elif choice == "2":
                rental_controller.rent_vehicle(user["UserID"])
            elif choice == "3":
                rental_controller.return_vehicle()
            elif choice == "4":
                rental_controller.show_customer_history(user["UserID"])
            elif choice == "0":
                print("👋 Auf Wiedersehen!")
                break
            else:
                print("⚠️ Ungültige Auswahl!")

        elif user["Role"] == "Employee":
            choice = menu.show_employee_menu()
            if choice == "1":
                vehicle_controller.show_all_vehicles()
            elif choice == "2":
                vehicle_controller.add_vehicle()
            elif choice == "3":
                vehicle_controller.update_price()
            elif choice == "4":
                rental_controller.show_customer_history_by_customerid()
            elif choice == "0":
                print("👋 Auf Wiedersehen!")
                break
            else:
                print("⚠️ Ungültige Auswahl!")


if __name__ == "__main__":
    main()
