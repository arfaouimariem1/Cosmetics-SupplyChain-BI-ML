"""Api resource module"""

from typing import NoReturn

from flask_restful import Api

from controllers.auth_controller import AuthController
from controllers.prediction_controller import DatePredictionController, PricePredictionController,DosagePredictionController
from src.controllers.alive_controller import AliveController
from utils.meta_singleton import MetaSingleton


class ApiResourceService(metaclass=MetaSingleton):
    """Manage API resource with Flask Restful"""

    api: Api = None

    def __init__(self, app):
        self.api = Api(app, prefix="/api", errors=self.__get_errors())

    def add_resources(self) -> NoReturn:
        """
        Adds API endpoints
        :return:
        """
        self.api.add_resource(AliveController, "/alive")
        self.api.add_resource(PricePredictionController, "/predict/price")
        self.api.add_resource(DosagePredictionController, "/predict/dosage")
        self.api.add_resource(DatePredictionController, "/predict/date")
        self.api.add_resource(AuthController, "/login")
        
    @staticmethod
    def __get_errors() -> dict:
        return {}
