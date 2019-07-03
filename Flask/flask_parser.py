import requests
from bs4 import BeautifulSoup

url = requests.get('http://localhost:8080/echo')
soup = BeautifulSoup(url.content, 'html.parser')

url1 = requests.post('http://localhost:8080/echo')
soup1 = BeautifulSoup(url1.content, 'html.parser')

print(soup,soup1)