from database.db_connection import  get_connection
import hashlib
import os
 
def hash_password(password, salt):
      return hashlib.sha256((salt + password).encode('utf-8')).hexdigest()  
 
class User:
    def __init__(self, name):
        self.name = name
 
    # def save(self):
    #     db = Database()
    #     db.connect()
    #     print(f"Benutzer {self.name} in Datenbank gespeichert")

    def save(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()
        print(f"Benutzer {self.name} in Datenbank gespeichert")
   
       
 
class UserModel:
    @staticmethod
    def get_user_by_credentials(username, password):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT * FROM User
                WHERE Username = ?
            """, (username,))
            user = cur.fetchone()
            conn.close()
           
            if user:
               salt = user["Salt"]
               hashed_input = hash_password(password,salt)
               if hashed_input == user["PasswordHash"]:
                return user
            return None
 
       
        except Exception as e:
            print(f"Fehler beim Login: {e}")
            return None
                 
 
    @staticmethod
    def save_user(username, password, role):
        conn = get_connection()
        salt = os.urandom(16).hex()
        password_hash = hash_password(password, salt)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO User (Username, PasswordHash, Salt, Role)
            VALUES (?, ?, ?, ?)
        """, (username, password_hash, salt, role))
        conn.commit()
        conn.close()