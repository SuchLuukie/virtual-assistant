# Import libraries
import flask
from flask_restful import Api

# Api endpoints
from endpoints.command import Command
from endpoints.login import Login
from endpoints.reminders import Reminders, RemindersExample
from endpoints.intent_update import Intent_update

# Portfolio endpoints
from portfolio.index import Index
from portfolio.cv import Cv
from portfolio.twentyfourtyeight import TwentyFourtyEight
from portfolio.minesweeper import Minesweeper
from portfolio.tictactoe import Tictactoe


class Server:
    def __init__(self):
        self.app = flask.Flask(__name__, template_folder="portfolio/templates", static_folder="portfolio/static")
        self.api = Api(self.app)

        # Add the API endpoints
        self.api.add_resource(Command, "/api/command")
        self.api.add_resource(Login, "/login")
        self.api.add_resource(Reminders, "/api/reminders")
        self.api.add_resource(RemindersExample, "/api/reminders/example")
        self.api.add_resource(Intent_update, "/api/intent_update")

        # Add the Portfolio endpoints
        self.api.add_resource(Index, "/")
        self.api.add_resource(Cv, "/CV.pdf")
        self.api.add_resource(TwentyFourtyEight, "/2048")
        self.api.add_resource(Minesweeper, "/minesweeper")
        self.api.add_resource(Tictactoe, "/tictactoe")


if __name__ == "__main__":
	Server().app.run(host="0.0.0.0", port=2205, debug=False)