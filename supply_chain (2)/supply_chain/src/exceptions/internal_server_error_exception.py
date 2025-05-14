from exceptions.app_exception import AppException


class InternalServerErrorException(AppException):
    def __init__(
        self,
        message: str = "Internal server error",
        description: str = "An unexpected error occurred on the server",
    ):
        super().__init__(message, description, 500)
