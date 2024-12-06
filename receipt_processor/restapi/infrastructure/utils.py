"""Utility methods shared across endpoints."""

import json

from flask_restx import Api
from flask_restx import Model


def process_schema(path: str, name: str, api: Api) -> Model:
    """Load a schema from a JSON file.
    
    Arguments:
        path: str
            A path-like to a JSON file.
        name: str
            The name of the schema. Should be a top-level element
            in the JSON file.

    Returns:
        The schema model
    """
    with open(path, 'r') as json_file:
        json_root = json.load(json_file)
    
    model_data = json_root[name]
    model = api.schema_model(name, model_data)
    api.add_model(name, model)
    
    return model
