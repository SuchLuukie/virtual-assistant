# Import libraries
from flask import request
from flask_restful import Resource
import datetime
import json
import jwt

# Import class
from authentication.encryption import Encryption

class Login(Resource):
    def __init__(self):
        self.secret_key = json.load(open("authentication/secret_key.json"))["key"]
        self.encryption = Encryption()


    def post(self):
        data = request.get_json(force=True)
        return self.verify_login(data["username"], data["password"])


    def verify_login(self, username, password):
        db = json.load(open("authentication/users.json"))
        for user in db:
            if db[user]["username"] == username:
                uuid = user

                if self.encryption.compare_password(uuid, password):
                    return {'Authorization': 'JWT {}'.format(self.generate_token(uuid))}
        
        return False
        

    def generate_token(self, uuid):
        db = json.load(open("authentication/users.json"))

        for entry in db:
            if entry == uuid:
                payload = db[uuid]
                payload.update({"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=5)})
                return jwt.encode(payload, self.secret_key)
