class AppException(Exception):
    """Base app exception"""

    def __init__(self, message: str, description: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.description = description
        self.status_code = status_code

    message = "Internal error"
    description = "An error occurred"
    status_code = 500
