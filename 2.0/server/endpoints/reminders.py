# Import libraries
from flask import request
from flask_restful import Resource
import json

# Import authentication
from authentication.authentication import auth, get_uuid_from_token

# Reminders endpoint
class Reminders(Resource):
    @auth.login_required
    def get(self):
        reminders = json.load(open("userData/userReminders.json"))
        
        try:
            return reminders[get_uuid_from_token(auth.current_user())]
        
        # If the user doesn't have any reminders
        except KeyError:
            return {}


    @auth.login_required
    def post(self):
        data = request.get_json(force=True)


class RemindersExample(Resource):
    @auth.login_required
    def get(self):
        return {
            "weekday": None,
            "time": None,
            "name": None,
            "description": None,
            "repeat": False
        }
