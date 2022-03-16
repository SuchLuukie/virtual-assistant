from flask import render_template, make_response
from flask_restful import Resource

# Minesweeper endpoint
class Minesweeper(Resource):
    def get(self):
        return make_response(render_template("minesweeper.html"))
