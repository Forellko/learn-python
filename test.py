import sys
import requests

response = requests.get('https://ya.ru/')

print(response.content)
