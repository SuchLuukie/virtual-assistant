# Import libraries
import flask
from flask_restful import Api

# Import endpoints
from endpoints.command import Command

class Server:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.api = Api(self.app)

        # Add the recources to the API
        self.api.add_resource(Command, "/command")


if __name__ == "__main__":
	Server().app.run(debug=True)