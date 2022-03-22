import requests
import time

data = {
    "username": "luuk tholen",
    "password": "test"
}

r = requests.post("http://127.0.0.1:5000/api/login", json=data)

print(r)
print(r.json())

command = {"command": "what time is it in the belgium"}
nr = requests.post("http://127.0.0.1:5000/api/command", json=command, headers=r.json())
print(nr)
print(nr.json())