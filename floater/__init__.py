import json
import logging
import os
import requests
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from .floater_support import FloatConverter, DateConverter


logger = logging.getLogger("collector.microservice")
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
api = Api(app)


class Converter(Resource):
    
    def __init__(self) -> None:
        self.object_types = {
            "float": FloatConverter(),
            "date": DateConverter()
        }
    
    def get(self, key):
        data = {}
        status_code = 200

        parser = reqparse.RequestParser()
        parser.add_argument("value", type=str, required=True, location="args")
        parser.add_argument("output_format", required=False, type=str, location="args")
        args = parser.parse_args()
        if key in self.object_types.keys():
            try:   
                params = [value for value in args.values() if value is not None]
                object_ = self.object_types.get(key, None)
                data = {"value": object_.convert(*params)}
            except Exception as e:
                data = str(e)
                status_code = 400
        else:
            data = "Page not found"
            status_code = 404
        
        return data, status_code


api.add_resource(Converter, "/convert/<key>")
