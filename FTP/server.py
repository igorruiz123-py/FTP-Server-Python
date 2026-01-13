from log import MyHandler
from pyftpdlib.servers import FTPServer
from db import DataBase
import threading
from time import sleep

class Server:
    def __init__(self) -> None:
        self.db = DataBase()
        self.handler = MyHandler
        self.host = ... # IPv4
        self.port = ... # Port
        self.running = True



    def loading_animation(self):
        dots = 0
        direction = 1
        while self.running:
            print(f"\rServer connected at Port {self.port}{'.' * dots}   ", end="")
            dots += direction
            if dots == 3:
                direction = -1
            elif dots == 0:
                direction = 1
            sleep(0.5)
            


    def run_server(self):

        auth = self.db.load_users_into_dummyauthorizer()

        self.handler.authorizer = auth

        server = FTPServer((self.host, self.port), self.handler)

        try:
            threading.Thread(target=self.loading_animation, daemon=True).start()
            server.serve_forever()
        except KeyboardInterrupt:
            self.running = False
            print("\nServer disconnected.")


if __name__ == "__main__":
    server = Server()
    server.run_server()
