import csv

file = open("name.csv")

reader = csv.reader(file)

for row in reader:
    print(row[0], '-', row[1])
