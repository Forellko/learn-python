import sys
import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(json.dumps(response.json(), indent=2))
