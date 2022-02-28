import requests
from requests.auth import HTTPBasicAuth

data = {
    "command": "What's the weather like"
}

r = requests.post("http://127.0.0.1:5000/command", json=data, auth=HTTPBasicAuth("luuk tholen", "test"))
print(r)
print(r.json())