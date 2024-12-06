"""Routes for /receipts endpoint."""

from typing import Any
import os

from flask_restx import Namespace
from flask_restx import Resource

from receipt_processor.restapi.infrastructure.utils import process_schema


api = Namespace('receipts', description='Process receipts')

# Load schema
path = os.path.join(os.path.dirname(__file__), 'schema.json')
Receipt = process_schema(path, 'Receipt', api)
ReceiptID = process_schema(path, 'ReceiptID', api)
Points = process_schema(path, 'Points', api)


@api.route('/process')
class Process(Resource):
    """Submits a receipt for processing."""

    @api.expect(Receipt, validate=True)
    @api.response(200, 'Returns the ID assigned to the receipt', ReceiptID)
    @api.response(400, 'The receipt is invalid')
    def post(self) -> Any:
        """Submits a receipt for processing."""


@api.route('/<id>/points')
class Points(Resource):
    """Returns the points awarded for the receipt."""

    @api.response(200, 'The number of points awarded', Points)
    @api.response(400, 'No receipt found for that id')
    def get(self, id: str) -> Any:
        """Returns the points awarded for the receipt."""
