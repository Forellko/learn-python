import csv

with open("name.csv") as file:
    reader = csv.reader(file)
    for read in reader:
        print(read)
