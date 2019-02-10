#!/usr/bin/python3
import requests

from config import config


headers = {
    "Content-type": "application/json"
}

data = {
    "text": "Wassssaaaap"
}

URL = config["default"]["webhook_url"]

response = requests.post(URL, json=data)

print("status", response.status_code)
print("body", response.text)
# print("status", response.status)

