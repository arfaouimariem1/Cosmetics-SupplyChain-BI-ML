from typing import NoReturn
from flask_restful import Api

from src.controllers.prediction_controller import CartonDamagePredictionController

from src.controllers.auth_controller import (
    AuthController,
    ProtectedManagerRoute,
    ProtectedProductionRoute,
    ProtectedVenteRoute
)
from src.controllers.prediction_controller import (
    DatePredictionController,
    PricePredictionController,
    DosagePredictionController,
    CartonDamagePredictionController,

)
from src.controllers.alive_controller import AliveController
from src.utils.meta_singleton import MetaSingleton

class ApiResourceService(metaclass=MetaSingleton):
    """Manage API resource with Flask Restful"""
    api: Api = None

    def __init__(self, app):
        self.api = Api(app, prefix="/api", errors=self.__get_errors())

    def add_resources(self) -> NoReturn:
        print("✅ Routes enregistrées")
        self.api.add_resource(AliveController, "/alive")
        self.api.add_resource(PricePredictionController, "/predict/price")
        self.api.add_resource(DosagePredictionController, "/predict/dosage")
        self.api.add_resource(DatePredictionController, "/predict/date")
        self.api.add_resource(AuthController, "/login")
        self.api.add_resource(ProtectedProductionRoute, "/protected/production")
        self.api.add_resource(ProtectedVenteRoute, "/protected/vente")
        self.api.add_resource(ProtectedManagerRoute, "/protected/manager")
        self.api.add_resource(CartonDamagePredictionController, "/predict/carton-damage")

 
    @staticmethod
    def __get_errors() -> dict:
        return {}
