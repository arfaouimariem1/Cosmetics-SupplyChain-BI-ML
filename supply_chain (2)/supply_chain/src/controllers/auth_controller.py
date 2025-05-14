from flask import Response, current_app, make_response, jsonify, request
from flask_restful import Resource
import jwt

from exceptions.app_exception import AppException
from services.auth_service import login
from utils.role_required import role_required

class AuthController(Resource):
    @staticmethod
    def post() -> Response:
        try:
            return make_response(jsonify(login()), 200)
        except AppException as e:
            return make_response(jsonify({"error": str(e)}), e.status_code)

class ProtectedProductionRoute(Resource):
    @staticmethod
    @role_required(['production', 'managerproduction'])
    def get():
        return jsonify({"message": "Bienvenue manager production !"})

class ProtectedVenteRoute(Resource):
    @staticmethod
    @role_required(['vente', 'managervente'])
    def get():
        return jsonify({"message": "Bienvenue manager vente !"})

class ProtectedManagerRoute(Resource):
    @staticmethod
    @role_required(['production', 'vente', 'managervente', 'managerproduction'])
    def get():
        auth_header = request.headers.get('Authorization')
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])

        role = decoded.get('role')

        messages = {
            "production": "Bienvenue au manager de production !",
            
            "vente": "Bienvenue au manager de vente !"
           
        }

        return jsonify({"message": messages.get(role, "Bienvenue manager !")})
