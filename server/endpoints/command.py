# Import libraries
from flask import request, Response
from flask_restful import Resource
import json
import re

# Import files
from intentClassification.intentClassifier import IntentClassifier
from commands.commands import Commands

# Import authentication
from authentication.authentication import auth, get_uuid_from_token

# Command endpoint
class Command(Resource):
    def __init__(self):
        self.operators = [
            "x",
            "*",
            "/",
            "+",
            "-"
        ]


    @auth.login_required
    def post(self):
        self.intent_classifier = IntentClassifier(self.operators)
        
        # Get users uuid and settings
        uuid = get_uuid_from_token(auth.current_user())
        user_settings = self.get_user_settings(uuid)

        # Initiate the commands with the users settings
        commands = Commands(user_settings, uuid, self.operators)

        # Get the command from the request
        try:
            text = request.get_json(force=True)["command"]
        
        # If the request doesnt have a command
        except KeyError:
            return Response(
                "No command entry has been found in the body",
                status=400
            )

        # Call intent classifier for it's prediction
        prediction = self.intent_classifier.predict(text)

        if "." in prediction:
            prediction = prediction.split(".")
            return getattr(getattr(commands, prediction[0]), prediction[1])(text)
            
        else:
            return getattr(commands, prediction)(text)


    # Returns the users settings
    def get_user_settings(self, uuid):
        return json.load(open("userData/userSettings.json"))[uuid]