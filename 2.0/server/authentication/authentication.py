# Import libraries
from flask_httpauth import HTTPTokenAuth

# Handle authentication
auth = HTTPTokenAuth(scheme='JWT')

#TODO
@auth.verify_token
def verify_token(token):
    return