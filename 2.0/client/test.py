import requests
import time

data = {
    "username": "luuk tholen",
    "password": "test"
}

r = requests.post("http://127.0.0.1:5000/login", json=data)

print(r)
print(r.json())

command = {"command": "whats the weather like bruv"}
nr = requests.post("http://127.0.0.1:5000/command", json=command, headers=r.json())
print(nr)
print(nr.json())