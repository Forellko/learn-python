import csv

with open("name.csv") as file:
    reader = csv.DictReader(file)
    for read in reader:
        print(read)
