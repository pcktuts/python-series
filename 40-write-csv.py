#40. Writing to CSV
import csv 

with open('employee.csv', 'a', newline='') as csvfile:
    fieldnames = ['name', 'age', 'salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    writer.writerow({'name': 'Arjun2', 'age': 25, 'salary': 35000})
    writer.writerow({'name': 'Kevin2', 'age': 27, 'salary': 32000})
