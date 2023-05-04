import csv

with open("name.csv", "a") as file:
    dictWriter = csv.DictWriter(file, fieldnames=['firstname', 'secondname'])
    dictWriter.writerow({"firstname": "1", "secondname": "2"})
