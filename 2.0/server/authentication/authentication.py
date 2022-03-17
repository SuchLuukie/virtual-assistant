# Import libraries
from flask_jwt_extended import verify_jwt_in_request
from flask_httpauth import HTTPTokenAuth
from flask_jwt_extended import get_jwt
import functools
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


def get_uuid_from_token(token):
    header_data = jwt.get_unverified_header(token)
    decoded = jwt.decode(
        token,
        secret_key,
        algorithms=[header_data["alg"], ]
    )
    return decoded["uuid"]


def is_admin(token):
    header_data = jwt.get_unverified_header(token)
    decoded = jwt.decode(
        token,
        secret_key,
        algorithms=[header_data["alg"], ]
    )
    return decoded["administrator"]