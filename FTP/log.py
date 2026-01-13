from pyftpdlib.handlers import FTPHandler
from datetime import datetime


class MyHandler(FTPHandler):
    def __init__(self, conn, server, ioloop=None):
        super().__init__(conn, server, ioloop)
        self.LOG_PATH = r"C:\Users\iruiz1\Desktop\FTP SERVER\Admins\Logs\connections\connections.log"


    def on_connect(self):

        time_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        ip, port = self.remote_ip, self.remote_port

        server_ip, server_port = self.server.address

        log = f"[{time_now}] CLIENT [{ip}:{port}] CONNECTED AT SERVER [{server_ip}:{server_port}]"

        print(log)
        print()

        with open(self.LOG_PATH, "a", encoding="UTF-8") as file:
            file.write(log + "\n")


    def on_login(self, username):

        time_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        ip = self.remote_ip

        log = f"[{time_now}] USER '{username}' LOGGED IN FROM {ip}"

        print(log)
        print()

        with open(self.LOG_PATH, "a", encoding="UTF-8") as file:
            file.write(log + "\n")


    def on_disconnect(self):
        
        server_ip, server_port = self.server.address

        time_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        username = getattr(self, "username", "Unknown")

        log = f"[{time_now}] USER '{username}' DISCONNECTED FROM SERVER [{server_ip}:{server_port}]"
        print(log)

        with open(self.LOG_PATH, "a", encoding="UTF-8") as file:
            file.write(log + "\n")