# Import libraries
import requests
import json

class ApiHandler:
    def __init__(self, gui):
        self.header = None
        self.gui = gui


    def login_request(self, username, password):
        data = {
            "username": username,
            "password": password
        }
        response = requests.post("http://127.0.0.1:5000/api/login", json=data)

        if response.status_code == 200:
            self.header = response.json()
            return True
        
        else:
            return False


    def command_request(self, text):
        command = {"command": text}
        nr = requests.post("http://127.0.0.1:5000/api/command", json=command, headers=self.header)

        if nr.status_code == 200:
            return nr.json()
        
        elif nr.status_code == 401:
            self.gui.initiate_logins()
            return