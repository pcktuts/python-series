#39 Reading CSV Files.
import csv
with open('employee.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'])
