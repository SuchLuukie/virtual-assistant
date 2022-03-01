# Import libraries
from flask_httpauth import HTTPTokenAuth
import datetime
import json
import jwt

# Handle authentication
auth = HTTPTokenAuth(scheme='JWT')
secret_key = json.load(open("authentication/secret_key.json"))["key"]

@auth.verify_token
def verify_token(token):
    try:
        header_data = jwt.get_unverified_header(token)
        decoded = jwt.decode(
            token, 
            secret_key, 
            algorithms=[header_data["alg"], ]
        )

        return token

    except jwt.ExpiredSignatureError:
        return False

    except jwt.InvalidSignatureError:
        return False