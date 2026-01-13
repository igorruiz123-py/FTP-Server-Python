from db import DataBase
from getpass import getpass
from os import system
from random import randint

class Admin:
    def __init__(self) -> None:
        self.db = DataBase()
        self.valid_commands = ["ins_user", "ins_admin", "has_user", "get_perms", "get_home_dir", "mk_report", "help", "exit"]
        self.commands = '''
ins_user [Insert new user into the data base]
ins_admin [insert new admin into the data base]
has_user [Return True if it has user in data base, False else]
get_perms [Return user permissions at the Server]
get_home_dir [Return the user directory path]
mk_report [Return report containing user informations]
'''
        self.cmd_user_name = None


    def administrate_users_entry(self):

        admin_user = input("admin@ftp~server $ Insert your administrator user > ")
        admin_password = getpass(f"{admin_user}@ftp~server $ Insert your administrator password > ")

        self.db.validate_admin_authentication(admin_user, admin_password)

        system("cls")

        cmd_help = input(f"{admin_user}@ftp~server $ (help to see commands) > ").lower()

        if cmd_help == "help":  
            print(self.commands)
            print()
        
        else:
            print(f"{cmd_help} is not recognized as an internal command.")
            print()

        while True:

            try:

                cmd_choose_command = input(f"{admin_user}@ftp~server $ (Type a command or help to see commands again, exit to break) > ").lower()

                if cmd_choose_command not in self.valid_commands:
                    print(f'"{cmd_choose_command}" is not recognized as an internal command.')
                    continue

                elif cmd_choose_command == "help":
                    print(self.commands)
                    print()

                elif cmd_choose_command == "ins_user":
                    
                    self.cmd_user_name = input(f"{admin_user}@ftp~server $ (Insert user first and last name) > ")
                    cmd_user_password = str(randint(1000, 9999))
                    cmd_user_perms = "elraw"
                    cmd_user_homw_dir = r"C:\Users\iruiz1\Desktop\FTP SERVER\Users"

                    self.db.insert_user(self.cmd_user_name, cmd_user_password, cmd_user_perms, cmd_user_homw_dir)

                elif cmd_choose_command == "ins_admin":

                    cmd_admin_name = input(f"{admin_user}@ftp~server $ (Insert user first and last name) > ")
                    cmd_admin_password = str(randint(1000, 9999))
                    cmd_admin_perms = "elradfmw"
                    cmd_admin_home_dir = r"C:\Users\iruiz1\Desktop\FTP SERVER\Admins"

                    self.db.insert_admin(cmd_admin_name, cmd_admin_password, cmd_admin_perms, cmd_admin_home_dir)

                elif cmd_choose_command == "has_user":

                    self.cmd_user_name = input(f"{admin_user}@ftp~server $ (Insert user name) > ")
                    
                    self.db.has_user(self.cmd_user_name)
                    print()

                elif cmd_choose_command == "get_perms":

                    self.cmd_user_name = input(f"{admin_user}@ftp~server $ (Insert user name) > ")

                    self.db.get_perms(self.cmd_user_name)
                    print()

                elif cmd_choose_command == "get_home_dir":

                    self.cmd_user_name = input(f"{admin_user}@ftp~server $ (Insert user name) > ")

                    self.db.get_home_dir(self.cmd_user_name)
                    print()

                elif cmd_choose_command == "mk_report":

                    self.db.make_report()
                    print()

                elif cmd_choose_command == "exit":
                    break

            except Exception as error:
                print(error)
                continue


if __name__ == "__main__":
    admin = Admin()
    admin.administrate_users_entry()
