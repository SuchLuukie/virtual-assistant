from flask import render_template, make_response
from flask_restful import Resource

# Index endpoint
class Index(Resource):
    def get(self):
        return make_response(render_template("index.html"))
