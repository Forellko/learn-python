import re

name = "Vladimir Demonov"

regex = re.search("(\w+) (\w+)", name)

firstname, lastname = regex.groups()

print(firstname, lastname)