import json
from flask import request

from exceptions.auth_exceptions import UserNotFoundException, MissingCredentialsException, InvalidPasswordException
from services.user_service import User


def login() -> dict:
    if not request.data:
        raise MissingCredentialsException
    auth_data: dict = json.loads(request.data)
    if not auth_data or not auth_data.get('email') or not auth_data.get('password'):
        raise MissingCredentialsException(description='Email and password are required')

    user = User.query \
        .filter_by(email=auth_data.get('email')) \
        .first()

    if not user:
        raise UserNotFoundException

    if user.password != auth_data.get('password'):
        raise InvalidPasswordException

    return {
        "status": "success",
        "message": "Successfully logged in.",
        "user": {
            "_id": user.id,
            "email": user.email,
            "fullname": user.fullname,
            "role": user.role
        }
    }

