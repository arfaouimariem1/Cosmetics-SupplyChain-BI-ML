from flask import Response, make_response, jsonify
from flask_restful import Resource

from exceptions.app_exception import AppException
from services.auth_service import  login


class AuthController(Resource):

    @staticmethod
    def post() -> Response:
        try:
            return make_response(jsonify(login()), 200)
        except AppException as e:
            return make_response(jsonify({"error": str(e)}),e.status_code )