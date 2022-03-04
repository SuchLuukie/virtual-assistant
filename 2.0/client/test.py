import requests
import time

data = {
    "username": "luuk tholen",
    "password": "test"
}

r = requests.post("http://127.0.0.1:5000/login", json=data)

print(r)
print(r.json())

#time.sleep(10)

nr = requests.get("http://127.0.0.1:5000/reminders", headers=r.json())
print(nr)
print(nr.json())