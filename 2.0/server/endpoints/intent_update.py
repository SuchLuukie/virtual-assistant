# Import libraries
from flask import request, Response
from flask_restful import Resource

# Import files
from intentClassification.intentClassifier import IntentClassifier

# Import authentication
from authentication.authentication import auth, is_admin

# Intent updating endpoint
class Intent_update(Resource):
    @auth.login_required
    def post(self):
        text = request.get_json(force=True)
        print(text)
        if not is_admin(auth.current_user()):
            return Response(
                "Administrator permission is required",
                status=403
            )

