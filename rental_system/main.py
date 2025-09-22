from controllers.user_controller import UserController
from controllers.vehicle_controller import VehicleController
from controllers.rental_controller import RentalController


def print_banner():
    car = r"""
        ______
       /|_||_\`.__
      (   _    _ _\
      =`-(_)--(_)-'
    """
    print("╔════════════════════════════════════╗")
    print("║   🚗  Vehicle Rental System V1.0   ║")
    print("╚════════════════════════════════════╝")
    print(car)
    print("\nWillkommen beim Vehicle Rental System!\n")


def main():
    print_banner()

    user_controller = UserController()
    user = user_controller.login()
    if not user:
        print("❌ Login fehlgeschlagen, Programm wird beendet.")
        return

    print(f"🎉 Eingeloggt als {user['Username']} ({user['Role']})")

    vc = VehicleController()
    rc = RentalController()
    role = user["Role"]

    while True:
        if role == "Customer":
            choice = user_controller.view.customer_menu()
            if choice == "1":
                rc.rent_vehicle(user["UserID"])
            elif choice == "2":
                vc.list_available()
            elif choice == "3":
                print("👋 Auf Wiedersehen!")
                break
            else:
                print("❌ Ungültige Eingabe!")

        elif role == "Employee":
            choice = user_controller.view.employee_menu()
            if choice == "1":
                rc.rent_vehicle(user["UserID"])
            elif choice == "2":
                vc.list_all()
            elif choice == "3":
                vc.add_vehicle()
            elif choice == "4":
                vehicle_id = int(input("Fahrzeug-ID: "))
                new_rate = float(input("Neuer Tagespreis (€): "))
                vc.model.update_price(vehicle_id, new_rate)
                print("✅ Preis aktualisiert!")
            elif choice == "5":
                rc.return_vehicle()
            elif choice == "6":
                print("👋 Auf Wiedersehen!")
                break
            else:
                print("❌ Ungültige Eingabe!")


if __name__ == "__main__":
    main()
