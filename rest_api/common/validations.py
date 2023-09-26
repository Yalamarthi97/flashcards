from functools import wraps
from flask import request, jsonify
import traceback
from jsonschema import validate, exceptions
import logging


def return_json_response(function):
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        response_object = None
        code = 200
        try:
            response_object, code = function(*args, **kwargs)
        except Exception as e:
            code = 500
            traceback.print_exc()
            response_object = {"error": "Something went wrong"}
            logging.error(str(e))
        return jsonify(response_object), code

    return wrapped_function


def schema_validation(schema):
    def wrap(function):
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            request_body = request.get_json()
            code = 200
            try:
                validate(instance=request_body, schema=schema)
            except exceptions.ValidationError as e:
                code = 500
                return {"error": "Incorrect values for {}".format(e.message)}, code
            return function(*args, **kwargs, request_body=request_body)

        return wrapped_function

    return wrap
