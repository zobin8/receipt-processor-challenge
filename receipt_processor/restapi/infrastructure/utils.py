"""Utility methods shared across endpoints."""

from functools import wraps
from typing import Callable
import json

from flask_restx import Api
from flask_restx import Model
from flask import request


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


def parse_type(arg: str, constructor: Callable):
    """Decorator to parse a type that is not handled by FLASK"""

    def decorator(func: Callable):
        """Decorator method. Modifies the decorated function."""

        wraps(func)
        def wrapper(*args, **kwargs):
            """Wrapper around function. Will convert the type"""
            try:
                request.json[arg] = constructor(request.json[arg])
            except Exception as e:
                return str(e), 400

            return func(*args, **kwargs)

        return wrapper

    return decorator