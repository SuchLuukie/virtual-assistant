# Import libraries
from flask import request
from flask_restful import Resource


# TODO
# Class to register a new user
class Register(Resource):
    def post(self):
        return