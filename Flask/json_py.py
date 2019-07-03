import json
import requests

url = requests.get('http://localhost:8080/country')
data=url.json()

print(data)