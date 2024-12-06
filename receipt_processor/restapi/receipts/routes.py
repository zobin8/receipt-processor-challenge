"""Routes for /receipts endpoint."""

from typing import Any
import os

from flask_restx import Namespace
from flask_restx import Resource

from receipt_processor.restapi.infrastructure.utils import process_schema


api = Namespace('receipts', description='Process receipts')

# Load schema
path = os.path.join(os.path.dirname(__file__), 'schema.json')
Item = process_schema(path, 'Item', api)
Receipt = process_schema(path, 'Receipt', api)


@api.route('/process')
class Process(Resource):
    """Submits a receipt for processing."""

    @api.expect(Receipt, validate=True)
    def post(self) -> Any:
        """Submits a receipt for processing."""


@api.route('/<id>/points')
class Points(Resource):
    """Returns the points awarded for the receipt."""

    def get(self, id: str) -> Any:
        """Returns the points awarded for the receipt."""
