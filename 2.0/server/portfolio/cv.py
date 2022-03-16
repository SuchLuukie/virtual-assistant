from flask import send_from_directory
from flask_restful import Resource

# Cv me endpoint
class Cv(Resource):
    def get(self):
        return send_from_directory("portfolio/static/assets/", "CV.pdf")
