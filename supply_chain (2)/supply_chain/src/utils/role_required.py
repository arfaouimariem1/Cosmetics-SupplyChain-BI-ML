from functools import wraps
from flask import request, jsonify, current_app
import jwt

def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({"message": "Token manquant"}), 401

            try:
                token = auth_header.split(" ")[1]
                decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
                if decoded.get('role') not in allowed_roles:
                    return jsonify({"message": "Accès refusé : rôle non autorisé"}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token expiré"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Token invalide"}), 401

            return f(*args, **kwargs)
        return wrapper
    return decorator


