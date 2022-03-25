# Import libraries
from flask import request, Response
from flask_restful import Resource
from csv import writer

# Import files
from intentClassification.intentClassifier import IntentClassifier

# Import authentication
from authentication.authentication import auth, is_admin

# Intent updating endpoint
class Intent_update(Resource):
    @auth.login_required
    def post(self):
        if not is_admin(auth.current_user()):
            return Response(
                "Administrator permission is required",
                status=403
            )

        # Get the intent and command from the request
        try:
            entry = request.get_json(force=True)
            intent = entry["intent"]
            command = entry["command"]

        # If the request doesnt have a command
        except KeyError:
            return Response(
                "No intent or command entry has been found in the body",
                status=400
            )

        with open('intentClassification/intentClassificationData.csv', 'a', newline='') as fd:
            writer_obj = writer(fd)
            writer_obj.writerow([intent.lower(), command.lower()])
            fd.close()

        return Response(
            "Succesfully added the intent",
            status=200
        )
