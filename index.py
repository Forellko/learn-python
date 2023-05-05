import re

email = '1111'

isValid = re.search(r"^1{0,3}$", email)

if isValid:
    print(1)
else:
    print(2)
