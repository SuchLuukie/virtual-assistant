import requests
import time

data = {
    "username": "luuk tholen",
    "password": "test"
}

r = requests.post("http://127.0.0.1:5000/api/login", json=data)

command = {"command": "tell me a joke"}
nr = requests.post("http://127.0.0.1:5000/api/command", json=command, headers=r.json())
print(nr)
print(nr.json())