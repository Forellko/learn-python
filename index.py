import csv

with open("name.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['1', '2'])
