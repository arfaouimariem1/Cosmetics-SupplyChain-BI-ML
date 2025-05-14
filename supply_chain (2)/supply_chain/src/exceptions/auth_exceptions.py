from exceptions.app_exception import AppException


class UserNotFoundException(AppException):
    def __init__(
        self, message: str = "User not found", description: str = "Could not find user"
    ):
        super().__init__(message, description, 404)


class MissingCredentialsException(AppException):
    def __init__(
        self,
        message: str = "Missing credentials",
        description: str = "Credentials could not be found in request payload",
    ):
        super().__init__(message, description, 400)


class InvalidPasswordException(AppException):
    def __init__(
        self,
        message: str = "Invalid password",
        description: str = "Provided password is invalid",
    ):
        super().__init__(message, description, 400)
