
from flask import Response, make_response, request, jsonify

from flask_restful import Resource
from exceptions.app_exception import AppException
from services.prediction_service import predictDosage, predictPrice, predictValidationDate

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
