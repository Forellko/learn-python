file = open('name.txt', 'r')

text = file.readlines()

for t in text:
    print(t.rstrip())
