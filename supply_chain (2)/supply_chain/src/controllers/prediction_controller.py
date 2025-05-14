
from flask import Response, make_response, request, jsonify

from flask_restful import Resource
from exceptions.app_exception import AppException
from services.prediction_service import predictDosage, predictPrice, predictValidationDate

from flask import request, jsonify, make_response, Response

from services.prediction_service import predictCartonDamage





class DatePredictionController(Resource):

    @staticmethod
    def post() -> Response:
        try:
            prediction_response = predictValidationDate(request.get_json())
            return make_response(jsonify(prediction_response),200)
        except AppException as e:
            return make_response(jsonify({"error": str(e)}),e.status_code )


class DosagePredictionController(Resource):

    @staticmethod
    def post() -> Response:
        try:
            prediction_dosage_response = predictDosage(request.get_json())
            return make_response(jsonify(prediction_dosage_response),200)
        except AppException as e:
            return make_response(jsonify({"error": str(e)}),e.status_code )

    
class PricePredictionController(Resource):

    @staticmethod
    def post() -> Response:
        try:
            prediction_response = predictPrice(request.get_json())
            return make_response(jsonify(prediction_response),200)
        except AppException as e:
            return make_response(jsonify({"error": str(e)}),e.status_code )
        
from flask import request, jsonify, make_response, Response
from flask_restful import Resource
from services.prediction_service import predictCartonDamage
from exceptions.app_exception import AppException

class CartonDamagePredictionController(Resource):
    @staticmethod
    def post() -> Response:
        try:
            print("📥 Requête reçue pour prédiction d'image")

            if 'image' not in request.files:
                raise AppException("Missing file", "An image file is required with key 'image'.", 400)

            image_file = request.files['image']
            image_bytes = image_file.read()
            result = predictCartonDamage(image_bytes)

            return make_response(jsonify({"result": result}), 200)

        except AppException as e:
            return make_response(jsonify({"error": str(e)}), e.status_code)
        except Exception as e:
            print("🔥 ERREUR INTERNE :", str(e))
            return make_response(jsonify({"error": "Internal error", "details": str(e)}), 500)


