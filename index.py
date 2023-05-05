import re

email = 'qwera'

isValid = re.search('.+@.+..+', email)

if isValid:
    print(1)
