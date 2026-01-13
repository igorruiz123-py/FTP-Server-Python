from pyftpdlib.authorizers import DummyAuthorizer

class Authorizer(DummyAuthorizer):
    def __init__(self, db) -> None:
        super().__init__()
        self.db = db
