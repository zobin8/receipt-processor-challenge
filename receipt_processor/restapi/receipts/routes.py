"""Routes for /receipts endpoint."""

from typing import Any

from flask_restx import Namespace
from flask_restx import Resource


api = Namespace('receipts', description='Process receipts')


@api.route('/process')
class Process(Resource):
    """Submits a receipt for processing."""

    def post(self) -> Any:
        """Submits a receipt for processing."""


@api.route('/<id>/points')
class Points(Resource):
    """Returns the points awarded for the receipt."""

    def get(self, id: str) -> Any:
        """Returns the points awarded for the receipt."""
