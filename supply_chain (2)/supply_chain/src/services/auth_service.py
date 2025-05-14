import json
from flask import request

from exceptions.auth_exceptions import UserNotFoundException, MissingCredentialsException, InvalidPasswordException
from services.user_service import User

import jwt
import datetime
from flask import request, current_app
from services.bcrypt_service import bcrypt



def login() -> dict:
    if not request.data:
        raise MissingCredentialsException

    auth_data: dict = json.loads(request.data)
    if not auth_data.get('email') or not auth_data.get('password'):
        raise MissingCredentialsException(description='Email and password are required')

    user = User.query.filter_by(email=auth_data.get('email')).first()

    if not user:
        raise UserNotFoundException

    # 🔒 Vérifier le mot de passe avec bcrypt
    if not bcrypt.check_password_hash(user.password, auth_data.get('password')):
        raise InvalidPasswordException

    # 🪪 Créer le token JWT
    token_payload = {
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "fullname": user.fullname,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }

    token = jwt.encode(token_payload, current_app.config['SECRET_KEY'], algorithm="HS256")

    return {
        "status": "success",
        "message": "Successfully logged in.",
        "token": token,
        "user": {
            "email": user.email,
            "fullname": user.fullname,
            "role": user.role
        }
    }


