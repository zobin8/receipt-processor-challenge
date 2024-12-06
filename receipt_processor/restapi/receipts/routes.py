"""Routes for /receipts endpoint."""

from datetime import date
from datetime import time
from typing import Any
import os

from flask_restx import Namespace
from flask_restx import Resource
from flask import request

from receipt_processor.backend.receipts.models import Receipt
from receipt_processor.backend.receipts.services import AddReceiptService
from receipt_processor.restapi.infrastructure.utils import process_schema
from receipt_processor.restapi.infrastructure.utils import parse_type


api = Namespace('receipts', description='Process receipts')

# Load schema
path = os.path.join(os.path.dirname(__file__), 'schema.json')
receipt_schema = process_schema(path, 'Receipt', api)
receipt_id_schema = process_schema(path, 'ReceiptID', api)
points_schema = process_schema(path, 'Points', api)


@api.route('/process')
class Process(Resource):
    """Submits a receipt for processing."""

    @api.expect(receipt_schema, validate=True)
    @parse_type('purchaseDate', date.fromisoformat)  # FLASK schemas do not parse dates
    @parse_type('purchaseTime', time.fromisoformat)  # FLASK schemas do not parse time
    @api.response(200, 'Returns the ID assigned to the receipt', receipt_id_schema)
    @api.response(400, 'The receipt is invalid')
    def post(self) -> Any:
        """Submits a receipt for processing."""
        rcpt = Receipt(**request.json)
        id = AddReceiptService().start(rcpt)
        if id is None:
            return 'Invalid Receipt', 400

        return dict(id=id)


@api.route('/<id>/points')
class Points(Resource):
    """Returns the points awarded for the receipt."""

    @api.response(200, 'The number of points awarded', points_schema)
    @api.response(400, 'No receipt found for that id')
    def get(self, id: str) -> Any:
        """Returns the points awarded for the receipt."""
