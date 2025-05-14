from exceptions.app_exception import AppException


class BadRequestException(AppException):
    def __init__(
        self,
        message: str = "Bad request",
        description: str = "The request is invalid or malformed",
    ):
        super().__init__(message, description, 400)
