from models.user_model import UserModel


class UserController:
    def __init__(self):
        self.model = UserModel()

    def login(self):
        print("🔑 Login")
        username = input("👉 Benutzername: ")
        password = input("👉 Passwort: ")
        user = self.model.get_user_by_credentials(username, password)
        if user:
            print(f"✅ Willkommen {user['Username']} ({user['Role']})")
        else:
            print("❌ Falsche Login-Daten!")
        return user
