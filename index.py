import re

email = 'aaaaab'

isValid = re.search(r"[^a]+[b]", email)

if isValid:
    print(1)
else:
    print(2)
