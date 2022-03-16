# Import libraries
from flask_restful import Resource
import json
import re

# Import files
from intentClassification.intentClassifier import IntentClassifier

# Import authentication
from authentication.authentication import auth, admin_required

# Intent updating endpoint
class Intent_update(Resource):
    @auth.login_required
    @admin_required
    def post():
        return