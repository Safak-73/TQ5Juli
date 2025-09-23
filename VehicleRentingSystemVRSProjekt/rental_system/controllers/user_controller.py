from models.user_model import UserModel
from views.main_menu import show_login_screen, show_login_failed, show_welcome
from views.customer_view import show_customer_menu
from views.employee_view import show_employee_menu
 
def login():
    username, password = show_login_screen()
    user = UserModel.get_user_by_credentials(username, password)
 
    if user:
        role = user[4]                  # Index 4 = Role
        show_welcome(role)
        if role == "Customer":
            show_customer_menu()
        elif role == "Employee":
            show_employee_menu()
        else:
            print("Unbekannte Rolle. Bitte wenden Sie sich an den Administrator.")
    else:
        show_login_failed()