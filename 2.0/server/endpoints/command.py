# Import libraries
from flask import request
from flask_restful import Resource

# Import authentication
from authentication.authentication import auth

# Command endpoint
class Command(Resource):
    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        return {"Success": True, "data": auth.current_user()}