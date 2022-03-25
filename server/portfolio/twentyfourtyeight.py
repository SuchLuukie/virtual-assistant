from flask import render_template, make_response
from flask_restful import Resource

# 2048 endpoint
class TwentyFourtyEight(Resource):
    def get(self):
        return make_response(render_template("2048.html"))
