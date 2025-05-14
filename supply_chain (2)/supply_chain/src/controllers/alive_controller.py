"""Module for checking app liveness"""

from flask import Response
from flask_restful import Resource


class AliveController(Resource):
    """Checks app liveness"""

    @staticmethod
    def get() -> Response:
        """Simple endpoint with no content response"""
        return Response(status=204)
