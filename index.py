import re

email = "dragonforce97q@gmail.com"

isValid = re.search(r'^.+@.+/..+$')

if isValid:
    print(1)
else:
    print(2)
