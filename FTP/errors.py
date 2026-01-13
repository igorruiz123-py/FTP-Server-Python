class InvalidUserNameError(Exception):
    def __init__(self, message = "User name must be first name + space + last name!") -> None:
        super().__init__(message)

class InvalidUserPasswordError(Exception):
    def __init__(self, message = "User password must be only 4 digits") -> None:
        super().__init__(message)

class InvalidAdminNameError(Exception):
    def __init__(self, message = "Admin name must be first name + space + last name!") -> None:
        super().__init__(message)

class InvalidAdminPasswordError(Exception):
    def __init__(self, message = "Admin password must be only 4 digits!") -> None:
        super().__init__(message)

class PermissionError(Exception):
    def __init__(self, message = "This permission is not assigned to regular users!") -> None:
        super().__init__(message)

class PathError(Exception):
    def __init__(self, message = "This directory path is not assigned to regular users!") -> None:
        super().__init__(message)