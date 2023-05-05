import re

email = 'dragonforce97q@gmail.com'

isValid = re.search(r"[a-z]+@[a-z]+\.[a-z]+", email)

if isValid:
    print(1)
else:
    print(2)
