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
        self.intent_classifier = IntentClassifier()
        self.operators = [
            "*",
            "/",
            "+",
            "-"
        ]


    @auth.login_required
    def post(self):
        # Get users uuid and settings
        uuid = get_uuid_from_token(auth.current_user())
        user_settings = self.get_user_settings(uuid)

        # Initiate the commands with the users settings
        commands = Commands(user_settings, uuid)

        # Get the command from the request
        try:
            text = request.get_json(force=True)["command"]
        
        # If the request doesnt have a command
        except KeyError:
            return Response(
                "No command entry has been found in the body",
                status=400
            )

        print(text)
        # Call intent classifier for it's prediction
        prediction = self.intent_classifier.predict(text)

        # Check if the text is a math question by looking for integers and operators
        has_math = self.contains_math(text)

        # Get the answer by executing the command
        if has_math:
            return commands.math(self.clean_text_for_math(text))

        return getattr(commands, prediction)()


    # Returns the users settings
    def get_user_settings(self, uuid):
        return json.load(open("userData/userSettings.json"))[uuid]


    # Returns intent prediction
    def predict_command(self, text):
        return self.intent_classifier.predict(text)

    
    # Check if there are integers or operators in a string.
    def contains_math(self, text):
        if re.search('\d', text):
            return True

        for operator in self.operators:
            if operator in text:
                return True

        return False


    # Cleans the text so only integers/floats and operators are in the text
    def clean_text_for_math(self, text):
        text = text.split(" ")

        clean_text = ""
        for element in text:
            if element in self.operators:
                clean_text += f" {element}"

            if re.search('\d', element):
                clean_text += f" {element}"

        return clean_text


	# Checks if a string is an integer
    def check_if_int(self, string):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()