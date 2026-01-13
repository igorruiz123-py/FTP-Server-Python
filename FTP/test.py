from random import randint
from pathlib import Path
import os
from time import sleep
import threading
import subprocess
import re


# # name = input("type your name: ")
# first_letter = name[0]
# first_name = ""
# last_name = ""
# space_found = False

# for char in name:
#     if char == " ":
#         space_found = True
#         continue
    
#     if not space_found:
#         first_name += char
#     else:
#         last_name += char

# random_number = randint(1, 9)
# user_name = (first_letter + last_name + str(random_number)).strip().upper()
# print(user_name)

# home = Path(r"C:\FTP SERVER\Users") / f"{user_name}"
# home.mkdir(parents=True, exist_ok=True)

# for subdir in ["uploads", "downloads"]:
#     (home / subdir).mkdir(parents=True, exist_ok=True)


# USER_DIR_PATH = Path(r"C:\FTP SERVER\Users")
# user_dir = USER_DIR_PATH / user_name

# print(user_dir)

# path_ = r"C:\FTP SERVER\Admins\IRUIZ4"

# # print(os.path.dirname(path_))

# PATH = fr"C:\FTP SERVER\Users\igor"
     
# if os.path.dirname(path_) != os.path.dirname(PATH):
#     print("Error!")
# else:
#     print("success!")




# def loading_animation():
#         dots = 0
#         direction = 1  # 1 = aumentando, -1 = diminuindo
#         while True:
#             print(f"\rServer connected at Port {"127.0.0.1"}{'.' * dots}   ", end="")
#             dots += direction
#             if dots == 3:    # quando chegar em 3 pontos, inverte
#                 direction = -1
#             elif dots == 0:  # quando chegar em 0 pontos, inverte
#                 direction = 1
#             sleep(0.5)


# threading.Thread(target=loading_animation, daemon=True).start()

# loading_animation()

# def validate_user_home_dir(path_: str, name: str):
     
#      USER_PATH = fr"C:\FTP SERVER\Users"
     
#      if path_ != USER_PATH:
#           print("Error")
#      else:
#         return print(os.path.join(USER_PATH, name))

# validate_user_home_dir(r"C:\FTP SERVER\Users", "igor")

# from datetime import datetime

# time_now = datetime.now().strftime("%H:%M:%S")

# ip = "192.168.100.10"
# port = 45412
# server_ip = "127.0.0.1"
# server_port = 2100


# with open(fr"C:\FTP SERVER\Admins\logs\connections.log", "w", encoding="UTF-8") as file:
#             file.write(f"[{time_now}] CLIENT [{ip}:{port}] CONNECTED AT [{server_ip}:{server_port}]")


# from db import DataBase

# db = DataBase()
# db.make_report()

# i = 0
# dots = 0
# direction = 1
# while i < 10:
#     print(f"\rChecking credentials{"." * dots} ", end="")
#     dots += direction
#     if dots == 3:
#         direction = -1
#     elif dots == 0:
#         direction = 1
#     sleep(0.5)
#     i += 1

# os.system("cls")

# i = 0
# dots = 0
# direction = 1
# while i < 10:
#     print(f"\rGetting access{"." * dots} ", end="")
#     dots += direction
#     if dots == 3:
#         direction = -1
#     elif dots == 0:
#         direction = 1
#     sleep(0.5)
#     i += 1

# os.system("cls")

# print("Access accepted")

# from getpass import getpass

# admin_user = input("admin@ftp~server $ Insert your administrator user > ")
# admin_password = getpass(f"{admin_user}@ftp~server $ Insert your administrator password > ")

# print(True)

# name = None

# x = input("Type y or z")

# if x == "y":
#     name = "igor"
#     print(name)
# elif x == "z":
#     name = "Nicolas"
#     print(name)

# from funcs import get_current_ip