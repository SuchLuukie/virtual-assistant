# Import libraries
from flask_httpauth import HTTPBasicAuth
import json

# Handle authentication
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    database = get_database()

    if username in database:
        if password == database[username]:
            return username
    return False


def get_database():
    return json.load(open("authentication/database.json"))