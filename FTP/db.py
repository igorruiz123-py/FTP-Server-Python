import sqlite3 as sql
from pathlib import Path
from funcs import (
validate_users_name, make_dir, validate_admins_name,
validate_user_home_dir, validate_admin_home_dir)
from pyftpdlib.authorizers import AuthenticationFailed, DummyAuthorizer
from time import sleep
import os


class DataBase:
    def __init__(self, *args, **kwargs) -> None:
        args, kwargs = args, kwargs
        self.DB_PATH = Path(__file__).parent / "FTP_data_base.db"
        self.TABLE_NAME_USERS = "users"
        self.TABLE_NAME_ADMINS = "admins"
        self.USER_DIR_PATH = Path(r"C:\Users\iruiz1\Desktop\FTP SERVER\Users")
        self.ADMIN_DIR_PATH = Path(r"C:\Users\iruiz1\Desktop\FTP SERVER\Admins")



    def open_connection(self):

        self.connection = sql.connect(self.DB_PATH)
        self.cursor = self.connection.cursor()



    def close_connection(self):

        self.cursor.close()
        self.connection.close()
        
            

    def loading_animation(self, phrase: str):

        i = 0
        dots = 0
        direction = 1
        while i < 10:
            print(f"\r{phrase}{'.' * dots} ", end="")
            dots += direction
            if dots == 3:
                direction = -1
            elif dots == 0:
                direction = 1
            sleep(0.5)
            i += 1

        os.system("cls")



    def create_tables(self):

        self.open_connection()

        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME_USERS}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT UNIQUE NOT NULL,
        user_password TEXT NOT NULL,
        user_permission TEXT NOT NULL,
        user_home_dir TEXT NOT NULL);''')

        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME_ADMINS}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        admin_name TEXT UNIQUE NOT NULL,
        admin_password TEXT NOT NULL,
        admin_permission TEXT NOT NULL,
        admin_home_dir TEXT NOT NULL);''')

        self.connection.commit()

        self.close_connection()



    def insert_user(self, name: str, password: str, perms: str, home_dir: str):

        self.open_connection()

        name = validate_users_name(name)

        make_dir(self.USER_DIR_PATH, name)

        home_dir = validate_user_home_dir(home_dir, name)

        self.cursor.execute(f'''
        INSERT INTO {self.TABLE_NAME_USERS} 
        (user_name, user_password, user_permission, user_home_dir)
        VALUES
        (?, ?, ?, ?);''', (name, password, perms, home_dir))

        self.connection.commit()

        self.loading_animation("Inserting User into data base")

        print("User inserted.")

        self.close_connection()


    def insert_admin(self, name: str, password: str, perms: str, home_dir: str):
         
         self.open_connection() 

         name = validate_admins_name(name) 

         make_dir(self.ADMIN_DIR_PATH, name)

         home_dir = validate_admin_home_dir(home_dir, name) 

         self.cursor.execute(f''' 
        INSERT INTO {self.TABLE_NAME_ADMINS}
        (admin_name, admin_password, admin_permission, admin_home_dir)
         VALUES (?, ?, ?, ?);''', (name, password, perms, home_dir))

         self.connection.commit() 

         self.loading_animation("Inserting Admin into data base") 

         print("Admin inserted.") 

         self.close_connection()



    def validate_authentication(self, user_name, password, handler=None):
        
        self.open_connection()

        self.cursor.execute(f'''
            SELECT user_name FROM {self.TABLE_NAME_USERS}
            WHERE user_name = ? AND user_password = ?''', (user_name, password))
        
        row = self.cursor.fetchone()

        self.close_connection()
        if row:
            return True
        else:
            raise AuthenticationFailed
        


    def has_user(self, user_name: str):

        self.open_connection()

        self.cursor.execute(f'''
        SELECT user_name FROM {self.TABLE_NAME_USERS}
        WHERE user_name = ?''', (user_name,))

        row = self.cursor.fetchone()

        self.close_connection()

        if row:
            print(True)
            return row[0]
        else:
            print(False)
            return False
        


    def get_perms(self, user_name):

        self.open_connection()

        self.cursor.execute(f'''
        SELECT user_permission FROM {self.TABLE_NAME_USERS}
        WHERE user_name = ?''', (user_name,))

        row = self.cursor.fetchone()

        self.close_connection()

        if row:
            print(row[0])
            return row[0]
        else:
            print(None)
            return None
        


    def get_home_dir(self, user_name):

        self.open_connection()

        self.cursor.execute(f'''
        SELECT user_home_dir FROM {self.TABLE_NAME_USERS}
        WHERE user_name = ?''', (user_name,))

        row = self.cursor.fetchone()

        self.close_connection()

        if row:
            print(row[0])
            return row[0]
        else:
            print(None)
            return None
        


    def make_report(self):

        self.open_connection()

        self.cursor.execute(f'''
        SELECT user_name, user_password, user_permission, user_home_dir FROM {self.TABLE_NAME_USERS}''')

        rows = self.cursor.fetchall()

        with open(r"C:\Users\iruiz1\Desktop\FTP SERVER\Admins\Logs\reports\report.log", "w", encoding="UTF-8") as file:
            for user_name, user_password, user_permission, user_home_dir in rows:
                file.write(f"User name: {user_name}\nUser password: {user_password}\nUser permission: {user_permission}\nUser home directory: {user_home_dir}\n")
                file.write("-" * 70 + "\n")

        print(r"report.log created at: C:\Users\iruiz1\Desktop\FTP SERVER\Admins\Logs\reports")

        self.close_connection()



    def load_users_into_dummyauthorizer(self):
       
        self.open_connection()

        auth = DummyAuthorizer()

        self.cursor.execute(f'''
            SELECT user_name, user_password, user_permission, user_home_dir FROM {self.TABLE_NAME_USERS}
        ''')

        rows = self.cursor.fetchall()

        for row in rows:

            user_name = row[0]
            user_password = row[1] if len(row) > 1 else ""
            user_permission = row[2] if len(row) > 2 and row[2] else "elradfmw"
            user_home_dir = row[3] if len(row) > 3 and row[3] else os.path.join(str(self.USER_DIR_PATH), user_name)

            
            user_home_dir = os.path.abspath(user_home_dir)

            os.makedirs(user_home_dir, exist_ok=True)

            try:
                auth.remove_user(user_name)
            except Exception:
                pass

            try:
                auth.add_user(user_name, user_password, homedir=user_home_dir, perm=user_permission)
                print(f"Added FTP user: {user_name} -> {user_home_dir} perm={user_permission}")
            except Exception as e:
                print(f"Failed to add user {user_name}: {e}")

        self.close_connection()
        return auth
    


    def validate_admin_authentication(self, name, password): 

        self.open_connection() 

        self.cursor.execute(f'''
        SELECT admin_name, admin_password FROM {self.TABLE_NAME_ADMINS}
        WHERE admin_name = ? AND admin_password = ?''', (name, password))

        row = self.cursor.fetchone()

        if row: 

            self.loading_animation("Checking credentials") 

            self.loading_animation("Getting access") 

            print("Access accepted!") 
            print() 

        else: 

            raise KeyError("User, password or both are incorrect!")
        
