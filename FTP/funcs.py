from re import match
from random import randint
from errors import (
     InvalidUserNameError, InvalidUserPasswordError, InvalidAdminNameError, InvalidAdminPasswordError, PermissionError,
     PathError)
from pathlib import Path
import os
import subprocess
import re


def validate_users_name(name: str):

        name_format = "^[A-Za-z]+ [A-Za-z]+$"

        if not match(name_format, name):
            raise InvalidUserNameError
        else:
            pass

        first_letter = name[0]
        last_name = ""
        space_found = False
        random_number = randint(1, 9)

        for char in name:
            if char == " ":
                space_found = True
                continue

            if not space_found:
                pass

            else:
                last_name += char

        user_name = (first_letter + last_name + str(random_number)).strip().upper()

        return user_name



def validate_admins_name(name: str):
    
    name_format = "^[A-Za-z]+ [A-Za-z]+$"

    if not match(name_format, name):
            raise InvalidAdminNameError
    else:
        pass

    first_name = ""
    space_found = False

    for char in name:
        if char == " ":
            space_found = True
            continue
        
        if not space_found:
            first_name += char
    
    admin_name = (first_name + "admin").strip().upper()

    return admin_name



def make_dir(path: Path, name: str):
    
    home = Path(path) / f"{name}"
    home.mkdir(parents=True, exist_ok=True)

    for subdir in ["uploads", "downloads"]:
        (home / subdir).mkdir(parents=True, exist_ok=True)



def validate_user_home_dir(path_: str, name: str):
     
     USER_PATH = Path.cwd() / "FTP SERVER" / "Users"
     
     if path_ != USER_PATH:
          raise PathError
     else:
        return os.path.join(USER_PATH, name)



def validate_admin_home_dir(path_: str, name: str):
     
    USER_PATH = Path.cwd() / "FTP SERVER" / "Admins"
     
    if path_ != USER_PATH:
          raise PathError
    else:
        return os.path.join(USER_PATH, name) 
    
       


