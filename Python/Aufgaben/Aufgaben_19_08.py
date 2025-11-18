import re

# Eingaben
permission = input("Enter your role: ")
level = 55  # Beispielwert, könnte auch dynamisch eingelesen werden

# Rolle bereinigen: Leerzeichen weg, Kleinbuchstaben, Sonderzeichen entfernen
role = re.sub(r'[^a-z]', '', permission.strip().lower())

# Geschäftsregeln
if role == "administrator":
    if level > 55:
        print("Welcome, Super Admin user.")
    else:
        print("Welcome, Admin user.")
elif role == "manager":
    if level >= 20:
        print("Contact an Admin for access.")
    else:
        print("You do not have sufficient privileges.")
else:
    print("You do not have sufficient privileges.")
