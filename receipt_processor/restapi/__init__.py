"""Submodule for restapi definition"""

from flask import Flask
from flask_restx import Api

from receipt_processor.restapi.receipts.routes import api as receipt_api


api = Api(
    title='Receipt Processor',
    description='A simple receipt processor',
)

api.add_namespace(receipt_api, '/receipts')

flask_app = Flask(__name__)
api.init_app(flask_app)
