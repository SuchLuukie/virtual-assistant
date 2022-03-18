import requests
import time

data = {
    "username": "luuk tholen",
    "password": "test"
}

r = requests.post("http://127.0.0.1:5000/api/login", json=data)

print(r)
print(r.json())

command = {"intent": "whats the weather like", "command": "weather_forecast"}
nr = requests.post("http://127.0.0.1:5000/api/intent_update", json=command, headers=r.json())
print(nr)
print(nr.json())