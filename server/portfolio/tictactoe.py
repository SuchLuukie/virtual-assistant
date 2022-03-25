from flask import render_template, make_response
from flask_restful import Resource

# Tictactoe endpoint
class Tictactoe(Resource):
    def get(self):
        return make_response(render_template("tictactoe.html"))
